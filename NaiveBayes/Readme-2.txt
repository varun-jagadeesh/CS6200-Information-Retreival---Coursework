README

CS 6200 – Information Retrieval
Assignment – 4
Naive Bayes Classifier
Language used:	Python

Libraries Used:
-glob
-math

Input Files:
textcat/train/pos/*.txt
textcat/train/neg/*.txt

Source code:
Training the model and generating the model file - naive_bayes_train.py
Prediction on the test based on the model generated from train - naive_bayes_test.py

File Name : naive_bayes_train (naive_bayes_train.py)
	    naive_bayes_test (naive_bayes_test.py)

Execution:  Execute file with command python filename.py


Output Files:

File Name: 	
model_file.txt - contains scores
dev_pos.txt - predictions for dev/pos directory
dev_neg.txt - predictions for dev/neg director
top_20_pos_neg_ratio.txt - list of top 20 terms with highest ratio of positive to negative top_20_neg_pos_ratio.txt -  list of top 20 terms with higest ratio of negative to positive

Percentage of positve and negative files	 

1. dev-pos
positive files in dev/pos - 72 
negative files in dev/pos - 28

2. dev-neg
positive files in dev/pos - 14 
negative files in dev/pos - 86

3. test
positive files in test - 86
negative fiels in test - 114

