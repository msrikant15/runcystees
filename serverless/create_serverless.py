import os

files = ["showTeeDesc.py", "showTeeReviews.py", "writeReview.py"]

try:
    # remove requests folder if exists
    # os.system("rm -rf requests")

    # unzip mysql and requests
    # os.system("unzip requests")

    for file in files:
        temp = file.split(".")[0]
        # remove root zipped folder if exist
        os.system("rm -rf " + temp)
        # remove existing folders
        os.system("rm -rf " + temp + "; rm -rf " + temp + ".zip")
        # create root folder
        os.makedirs(temp)
        # copy the python file, requests, urllib3, idna, chardet, certifi folders to root
        # os.system('cp -a requests ' + temp + '; cp -a urllib3 ' + temp + 
        # '; cp -a idna ' + temp + '; cp -a chardet ' + temp + 
        # '; cp -a certifi ' + temp + '; cp ' + file + ' ' + temp)
        os.system('cp ' + file + ' ' + temp)
        # move to root folder and zip contents
        os.system('cd ' + temp + '; zip -r ' + temp + '.zip *; mv ' + temp + '.zip ../')
        # remove root folder
        os.system("rm -rf " + temp)

    # remove requests, urllib3, idna, chardet, certifi unzipped folder if exists
    # os.system("rm -rf requests")
    # os.system("rm -rf urllib3")
    # os.system("rm -rf idna")
    # os.system("rm -rf chardet")
    # os.system("rm -rf certifi")

except Exception as e:
    print(e)
