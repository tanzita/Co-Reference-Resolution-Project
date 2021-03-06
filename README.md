# Co-Reference Resolution Project

In this exercise I tried to implement a machine learning classifier based on the methods described in Soon et al. (2001: A Machine Learning Approach to Coreference Resolution of Noun Phrases). I used OntoNotes, CoNLL-2012 data as training and test data. I used Support Vector Machine (SVM) classifier using scikit-learn toolkit in python to predict the output. I chose SVM because Decision Tree classifier has a tendency to become over-fitted easily and SVM is quite effective in binary boundary detection. 

## Determination of Markables

I chose the following items as the components for each NP phrases in the input data (both test and training data),

* Words
* Parts of Speech
* Name-Entity Values (‘null’ if not present)
* Coreference Chain Number (‘null’ if not present)
* Sentence Number

Also each begin statement of a file segment is kept for future calculation.

The files in where the markables are stored are named as follows,

* training_markables
* test_markables

Each line in the file represents a NP phrases except the file boundary lines.  For example a file boundary line,

#begin document (wb/eng/00/eng_0009); part 000

In the corpus all the name-entity valued word segments were inside the related noun phrase. So I did not check the ‘Nested noun phrase extraction’ because it has already been done.

As I have considered every noun phrases (denoted as NP) in our code (markable_extraction.py) so I am sure that the precision and recall will be 100%.

## Evaluation

I have evaluated the predicted data using sklearn.metrics module and obtained the following results 
* Accuracy = 96.1963771458%
* Precision = 84.0616966581%
* Recall = 28.7671232877%
* F1-Score = 42.8651685393%

## Guideline to use the scripts

This Read-Me file describes a step-by-step guideline to use the following six scripts-

* feature_extraction.py
* markable_extraction.py
* markable_extraction_big_data.py
* run_steps.sh
* run_steps_big_data.sh
* svm-classification.py

1. Please keep all the scripts in a same directory and do not change their names. 


2. a. If your input data (training data and test data) are small in size then you should run the ‘run_steps.sh’ script. You have to provide the data file names (with location if it is in a different directory) after that.
      
      Or,
   
   b. If your input data (training data and test data) are big in size then you should run the ‘run_steps.sh_big_data’ script. 
   
   It is important to note that, in this case the exact names of the training data and test data files are as follows:
      
         I. ontonotes-train.conll
         II. ontonotes-test.conll
         
      Please keep these two files in the same directory where all the scripts are kept. 
      
      If you want to change their names then please change it manually before executing on line number 358 and 362 in markable_extraction_big_data.py script.
      
      Please use the following command to run the script,
      
        nohup sh run_steps.sh_big_data &

      You can see the execution update in the nohup.out file.

3. Output will be generated in the output folder. The 12 files are as follows,

* training_markables
* test_markables
* training_data_Positive_chain_lines
* training_data_Negative_chain_lines
* test_data_Positive_chain_lines
* test_data_Negaitive_chain_lines
* training_features
* test_features
* test_data_predicted_classes
* test_data_Positive_chain_lines_with_predicted_classes
* test_data_Negaitive_chain_lines_with_predicted_classes
* Evaluation

Please do not remove them or change their names unless you can see the following message in the terminal or nohup.out file-

          SVM classification is finished, Please see the output files
          Thanks a lot for your time
