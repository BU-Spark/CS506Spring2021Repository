import swifter
import numpy as np
import pandas as pd
import seaborn as sns
import re
from csv import writer
import copy
import os 
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PolynomialFeatures
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import mean_squared_error, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import mysql.connector

mydb = mysql.connector.connect(host='73.38.248.152', user='buspark', password='U@5p1r3!')

if (mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()


# Load sql to dataframe 
# Get Training Set (Action != NULL and Actor != NULL)
# Getting 10000 values first 
case_index_not_null = pd.read_sql("SELECT c_a_index.actor, c_a_index.action, c_a_index.description FROM wp_courtdocs.cdocs_case_action_index as c_a_index where c_a_index.actor != ' ' and c_a_index.action != ' ' and c_a_index.description != ' ' LIMIT 50000", con = mydb)
columns = ['action','description']
trainSet = case_index_not_null[columns]
print(trainSet.head())
print(trainSet.shape)


# Get Test Set (Action = NULL)
# Getting 10000 values first 
action_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action = ' ' and c_a_index.description != ' ' LIMIT 10000;", con = mydb)
testSet = action_null[columns]
print(testSet.head())

# Get Distinct Values of Actions Field with Index Number 
path1 = "C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\distinct-case-actions.txt"
distinct_actions = pd.read_csv(path1)
print(distinct_actions.head())

#merge training set with distinct-case-actions.txt to get the index value for distinct actions 
trainSet = trainSet.merge(distinct_actions, on='action')
print(trainSet.head())

# r = re.compile(r'[^\w\s]+')
# trainSet['description'] = [r.sub('', x) for x in trainSet['description'].tolist()]
# trainSet['description'] = trainSet['description'].str.lower().str.split()
# print(trainSet.head())

# testSet['description'] = [r.sub('', x) for x in testSet['description'].tolist()]
# testSet['description'] = testSet['description'].str.lower().str.split()
# print(testSet.head())

# stopwords = stopwords.words('english')
# #remove stopwords in trainSet 
# trainSet['description'] = trainSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
# print("stopwords")
# print(trainSet.head())
# print()

# #remove stopwords in testSet 
# testSet['description'] = testSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
# print(testSet.head())

#use Lemmatizer for train and test set 
#lemmatizer = WordNetLemmatizer() 
#trainSet['description'] = trainSet['description'].apply(lambda x:[lemmatizer.lemmatize(word) for word in x])
#testSet['description'] = testSet['description'].apply(lambda x:[lemmatizer.lemmatize(word) for word in x])

#remove duplicate words after lemmatizing 
#trainSet['description'] = trainSet['description'].apply(lambda x:list(dict.fromkeys(x)))
#print()
#print('trainingSet after lemmatizer & removing dupes ')
#print(trainSet.head())

#testSet['description'] = testSet['description'].apply(lambda x:list(dict.fromkeys(x)))
#print()
#print('testSet after lemmatizer & removing dupes ')
#print(testSet.head())

#copy
trainSet1 = copy.deepcopy(trainSet)
testSet1 = copy.deepcopy(testSet)

# #join back 
# trainSet1['description'] = trainSet1 ['description'].apply(lambda x:' '.join(x))
# testSet1['description'] = testSet1['description'].apply(lambda x:' '.join(x))
# print()

# trainSet1['description'] = trainSet1['description'].astype('str')
# testSet1['description'] = testSet1['description'].astype('str')

print("preprocessing done")
print(trainSet1.head())
print(testSet1.head())

#train-test-split starts 
X = trainSet1['description']
y = trainSet1['action_index']

print("train-test-split processing")
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

clf1 = Pipeline([('tfidf', TfidfVectorizer()),('rdf',RandomForestClassifier()),])
# training data through the pipeline
clf1.fit(X_train, y_train)


clf2 = Pipeline([('tfidf', TfidfVectorizer()),('mnb',MultinomialNB()),])
# training data through the pipeline
clf2.fit(X_train, y_train)

#RandomForest Prediction 
prediction1 = clf1.predict(testSet1['description'])
print(prediction1.shape)
print() 
#score: 0.025610244097639057

print(accuracy_score(y_test, prediction1[:9996]))

#MultinomialNB Prediction 
prediction2 = clf2.predict(testSet1['description'])
print(prediction2.shape)

print(accuracy_score(y_test, prediction2[:9996]))
#score: 0.0858343337334934

submission1 = pd.DataFrame({'description':testSet1['description'],'action_index':prediction1})
#Visualize the first 5 rows
print("prediction 1")
print(submission1.head())
submission1 = submission1.merge(distinct_actions, on='action_index') 

submission2 = pd.DataFrame({'description':testSet1['description'],'action_index':prediction2})
print("prediction 2")
print(submission2.head())
submission2 = submission2.merge(distinct_actions, on='action_index') 

path4 = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\RandomForest-Prediction.txt'
path5 = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\MultinomialNB-Prediction.txt'
submission1.to_csv(path4, mode='w', index = False)
submission2.to_csv(path5, mode='w', index = False)
#testSet1.to_csv(path3, mode='w', index = False, header = False)

