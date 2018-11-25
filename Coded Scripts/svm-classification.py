import sys
import numpy as np
from sklearn import cross_validation
from sklearn import svm
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

# Written by Tanzia Haque Tanzi

training_data = np.loadtxt("output/training_features", delimiter=",")

training_data_features = training_data[:, 1:]  # select all the Features in training data
training_data_labels = training_data[:, 0]   # select all the target classes in training data

test_data = np.loadtxt("output/test_features", delimiter=",")

test_data_features = test_data[:, 1:]  # select all the Features in test data
test_data_labels_original = test_data[:, 0]   # select all the target classes in test data



#training the data in the classifier
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(training_data_features, training_data_labels)

#calculating the prediction
test_data_labels_prediction = clf.predict(test_data_features)

sys.stdout = open("output/Evaluation", 'w')
#calculating the evaluation
accuracy = accuracy_score(test_data_labels_original, test_data_labels_prediction)
precision = precision_score(test_data_labels_original, test_data_labels_prediction, average='binary') 
recall = recall_score(test_data_labels_original, test_data_labels_prediction, average='binary') 
f1_score = f1_score(test_data_labels_original, test_data_labels_prediction, average='binary')

print "Accuracy = " + str(accuracy * 100) +"%"
print "Precision = " + str(precision * 100) +"%"
print "Recall = " + str(recall * 100) +"%"
print "F1-Score = " + str(f1_score * 100) +"%"

#printing the values with test data
test_data_labels_prediction_list = test_data_labels_prediction.tolist()

sys.stdout = open("output/test_data_predicted_classes", 'w')
for item in test_data_labels_prediction_list:
    print item

sys.stdout = open("output/test_data_Positive_chain_lines_with_predicted_classes", 'w')

raw_data = open("output/test_data_Positive_chain_lines")   
file_data = raw_data.read().split('\n')
raw_data.close()

negative_data_length = len (file_data) - 1


for line_index in range (len (file_data)-1):
    print file_data[line_index] + " |**| " + str(test_data_labels_prediction_list[line_index])

sys.stdout = open("output/test_data_Negaitive_chain_lines_with_predicted_classes", 'w')

raw_data = open("output/test_data_Negaitive_chain_lines")   
file_data = raw_data.read().split('\n')
raw_data.close()
  
for line_index in range (len (file_data)-1):
    print file_data[line_index] + " |**| " + str(test_data_labels_prediction_list[line_index + negative_data_length])

