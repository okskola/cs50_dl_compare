# cs50_dl_compare

This is a Python script to run in Codespaces to download all students submissions and check them with compare50.

Usage:

* Create Codespaces for the repository
* Run pip install compare50
* In Github Codespace secrets (https://github.com/USERNAME/REPOSITORY/settings/secrets/codespaces) you must create two secrets: GIT_USERNAME and GIT_TOKEN (create token here https://github.com/settings/tokens).
* From submit.cs50.io (https://submit.cs50.io/courses/COURSEID/) download csv file
* Make it private so students do not see uploaded solutions
* Upload archived solutions to the "archived" folder
* Copy/paste csv contents to the dl.csv file
* Run Python script dl.py
* Download results.zip, unzip and check the comparison results locally
* Delete folders 'student_files' and 'results' and delete results.zip
