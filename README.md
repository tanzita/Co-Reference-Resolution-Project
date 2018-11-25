# Co-Reference-Resolution-Project

Guideline to use the scripts

This Read-Me file describes a step-by-step guideline to use the following six scripts-

* feature_extraction.py
* markable_extraction.py
* markable_extraction_big_data.py
* run_steps.sh
* run_steps_big_data.sh
* svm-classification.py

These scripts were created by Mahbub Ul Alam (3144196) & Tanzia Haque Tanzi (3144251) for the project work for the ‘Co-Reference Resolution’ in SS-2016 (MSc. In CL at IMS). For details about the work, scripts and output please see the ‘Project Report’ document.

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
