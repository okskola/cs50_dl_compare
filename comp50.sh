#!/bin/bash 

#pip install compare50


echo "Starting compare"
compare50 * -x "dl.csv" -x "dl.py" -x "comp50.sh" 
echo "Done compare"
zip -r results.zip results/
echo "Done zipping. Please download results.zip"
