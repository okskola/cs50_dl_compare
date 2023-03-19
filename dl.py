# This is a Python script to run in Codespaces to download all students submissions and check them with compare50.
#
# MIT License
# Copyright (c) 2023 https://github.com/okskola

import requests
import re
import zipfile 
import csv
import os

username = os.environ['GIT_USERNAME']
token = os.environ['GIT_TOKEN']

print("Starting")

with open('dl.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        archive = row["archive"]

        r = requests.get(archive, auth=(username,token))
        #print( r.headers )
        fname = re.findall("filename=(.+)", r.headers['content-disposition'])[0]
        print( fname )
        open(fname, 'wb').write(r.content)
        r.close()
        with zipfile.ZipFile(fname, 'r') as zipObj:
            zipObj.extractall()
        os.remove(fname) 
print("Download completed, running compare50")
os.system('compare50 * -x "dl.csv" -x "dl.py" -x "comp50.sh"')
print("Compare50 finished, archiving 'results' folder")
os.system("zip -r results.zip results/")
print("Done! Please download 'results' archive.")
print("After that remove data from csv and delete all student folders including 'results' folder and file.")
