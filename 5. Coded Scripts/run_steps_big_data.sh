#!/bin/bash

#=====================================================================================
#Project Work for "Co-reference Resolution" course-
#this script is a step by step procedure to extract the features
#and classify them using SCI-Kit tool in SVM.
#for details please see the documentation report.

# Written by Tanzia Haque Tanzi
#=====================================================================================

export LC_ALL=C

echo "==============================================================
#Project Work for 'Co-reference Resolution' course-
#this script is a step by step procedure to extract the features
#and classify them using SCI-Kit tool in SVM.
#for details please see the documentation report.
====================================================================

"

echo "
===========================================================================
#Extracting the markables (It may take a long amount of time)..........
==========================================================================

"

#creating the 'output' directory
if [ -d "${PWD}/output" -a ! -h "${PWD}/output" ]
then
   rm -r output; mkdir output 
else
   mkdir output
fi

#this script will extract the markables from training data and test data
chmod +x markable_extraction_big_data.py
python markable_extraction_big_data.py

echo "
==================================================================================
#Markables are Successfully Extracted
#Now creating the feature data (It may take a long amount of time).............
=================================================================================

"
#this script will create the feature data
chmod +x feature_extraction.py
python feature_extraction.py


echo "
===========================================================================
#Feature data files have been successfully created
#Now running the classifier (It may take a long amount of time)..........
==========================================================================

"

#this script will compute the SVM classification and print the evaluation result.
chmod +x svm-classification.py
python svm-classification.py

echo "
=============================================================
#SVM classification is finished, Please see the output files
#Thanks a lot for your time
=============================================================
"
