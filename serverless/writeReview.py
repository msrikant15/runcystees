import boto3
import requests
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def getEBSFromOrgID(orgid):
    try:
        # Credentials to access DynamoDB associated with IAM policy 
        # This IAM policy inturn is tied to Lambda for proper permission access
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('funnelconfig')

        # When adding a global secondary index to an existing table, you cannot query the index until it has been backfilled.
        # This portion of the script waits until the index is in the “ACTIVE” status, indicating it is ready to be queried.
        # while True:
        #     if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        #         print('Waiting for index to backfill...')
        #         time.sleep(5)
        #         table.reload()
        #     else:
        #         break

        resp = table.query(
            # Global Secondary Index (GSI) named "OrgIDIndex" was created by the script add_secondary_index.py
            # This was executed manually (just once) after the table was created
            IndexName="OrgIDIndex",
            KeyConditionExpression=Key('OrganizationID').eq(orgid))

        if int(resp['Count']) == 0:
            return {"result": False}

        return {"result": True, "ebs": resp['Items'][0]['APIEndpoint']}
    except ClientError as e:
        return {"result": "Error occurred"}
        print("Error occurred - getEBSFromOrgID(", orgid, ") - ", e.response)

def execebsrequest(ebs, fn, reqtype, payload):
    if reqtype == 'get':
        url = ebs + '/' + fn
        r = requests.get(url)
        return r.json()
    if reqtype == 'delete':
        url = ebs + '/' + fn
        r = requests.delete(url)
        return r.json()
    if reqtype == 'post':
        url = ebs + '/' + fn
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return r.json()
    if reqtype == 'put':
        url = ebs + '/' + fn
        headers = {'content-type': 'application/json'}
        r = requests.put(url, data=json.dumps(payload), headers=headers)
        return r.json()

def lambda_handler(event, context):
    orgid, fn, reqtype, payload = "", "", "", ""
    if 'orgid' in event:
        orgid = event['orgid']
    if 'fn' in event:
        fn = event['fn']
    if 'reqtype' in event:
        reqtype = event['reqtype']
    if 'payload' in event:
        payload = event['payload']

    ebsres = getEBSFromOrgID(orgid)
    if ebsres['result'] == True:
        ebs = ebsres['ebs']
    else:
        return ebsres

    return execebsrequest(ebs, fn, reqtype, payload)
