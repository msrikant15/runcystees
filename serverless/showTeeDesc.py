import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def showTeeDesc(id):
    try:
        # Credentials to access DynamoDB is associated with IAM role 
        # This IAM role inturn is tied to Lambda for proper permission access
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('runcystees')

        resp = table.get_item(Key={"id": id})

        if resp.get('Item') == None:
            return {"result": False}

        return {"result": True, "desc": resp['Item']['desc']}
    except ClientError as e:
        return {"result": "Error occurred"}
        print("Error occurred - showTeeDesc(", id, ") - ", e.response)

def lambda_handler(event, context):
    id = ""
    if 'id' in event:
        id = event['id']

    teeinfo = showTeeDesc(id)
    return teeinfo
