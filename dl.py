username = 'xxx'
token = 'xxx'

import requests
import re
import zipfile 
import csv
import os


print("Sākums")

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
