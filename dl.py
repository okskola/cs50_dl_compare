# This is a Python script to run in Codespaces to download all students submissions and check them with compare50.
#
# MIT License
# Copyright (c) 2023 https://github.com/okskola
#
# Warning! Almost no error checking done. Use at your own risk.
#

import re
import zipfile 
import csv
import os
import requests

username = os.environ['GIT_USERNAME']
token = os.environ['GIT_TOKEN']
filesdir = "student_files"
distrdir = "distr"
archir = "archived"

print("Starting")
folder = input("Folder name for archived and distributed files (empty for none):")

try:
    os.mkdir(filesdir)
except OSError:
    # folder already exists at the destination
    pass

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
            zipObj.extractall(filesdir)
        os.remove(fname) 
print("Download completed, running compare50")
#os.system('compare50 * -x "dl.csv" -x "dl.py" -x "comp50.sh"')
if len(folder) == 0:
    os.system('compare50 '+os.path.join(filesdir, '*'))
else:
    os.system( 'compare50 '+os.path.join( filesdir,'*' ) + 
              " -d " + os.path.join( distrdir, folder, '*' ) + 
              " -a " + os.path.join( archir, folder, '*' ) )

print("Compare50 finished, archiving 'results' folder")
os.system("zip -r results.zip results/")
print("Done! Please download 'results' archive.")
print("Then remove data from csv, delete folders 'student_files' and 'results' and delete results.zip.")
