import os

files = ["showTeeDesc.py"]

try:
    for file in files:
        temp = file.split(".")[0]
        # remove root zipped folder if exist
        os.system("rm -rf " + temp)
        # remove existing folders
        os.system("rm -rf " + temp + "; rm -rf " + temp + ".zip")
        # create root folder
        os.makedirs(temp)
        # copy the python file
        os.system('cp ' + file + ' ' + temp)
        # move to root folder and zip contents
        os.system('cd ' + temp + '; zip -r ' + temp + '.zip *; mv ' + temp + '.zip ../')
        # remove root folder
        os.system("rm -rf " + temp)
except Exception as e:
    print(e)
