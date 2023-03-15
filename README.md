# cs50_dl_compare

This is a Python script to run in Codespaces to download all students submissions and check them with compare50.

Usage:

* In Github https://github.com/USERNAME/REPOSITORY/settings/secrets/codespaces you must create two secrets: GIT_USERNAME and GIT_TOKEN (create token here https://github.com/settings/tokens).
* From https://submit.cs50.io/courses/COURSEID/ download csv file
* Rename csv as dl.csv 
* Run Python script dl.py
* Download results.zip, unzip and check the compare results locally
* Delete results.zip and all folders from repository
