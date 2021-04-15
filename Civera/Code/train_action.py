import swifter
import numpy as np
import pandas as pd
import seaborn as sns
import re
import math
from csv import writer
import copy
import os 
import matplotlib.pyplot as plt
import nltk
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
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from sklearn.metrics import accuracy_score
import mysql.connector

mydb = mysql.connector.connect(host='', user='', password='')

if (mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

#code for new custom training Set
# SELECT distinct(c_a_index.action) ,
#        count(c_a_index.description),
#        ROUND(count(c_a_index.description) * 0.01,0) as rounded
# FROM wp_courtdocs.cdocs_case_action_index as c_a_index
# where c_a_index.action != " "  and c_a_index.actor != " " 
# group by c_a_index.action 

# Load sql to dataframe 
# Get Training Set (Action != NULL and Actor != NULL)
# Getting 50000 values first 
custom_training = pd.read_csv("C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\custom-training.txt", error_bad_lines=False)


query1 = '''SELECT c_a_index.actor, c_a_index.action , c_a_index.description, c.description as preprocessed_desc FROM wp_courtdocs.cdocs_case_action_index as c_a_index INNER JOIN wp_courtdocs_NORMALIZED.distinct_case_actions as c on c_a_index.action = c.action where c_a_index.action != " "  and c_a_index.actor != " " and c_a_index.description REGEXP  (SELECT GROUP_CONCAT(c.description SEPARATOR '|') FROM wp_courtdocs_NORMALIZED.distinct_case_actions as c) and RAND() LIMIT 50000'''
case_index_not_null = pd.read_sql_query(query1,mydb)
columns = ['action','description','preprocessed_desc']
trainSet3 = case_index_not_null[columns]
#print(trainSet1.head())


# Get Test Set (Action = NULL)
# Getting 10000 values first 
query2 = '''SELECT c_a_index.actor, c_a_index.action , c_a_index.description FROM wp_courtdocs.cdocs_case_action_index as c_a_index where c_a_index.action = " " and c_a_index.description REGEXP  (SELECT GROUP_CONCAT(c.description SEPARATOR '|') FROM wp_courtdocs_NORMALIZED.distinct_case_actions as c) LIMIT 1000'''
action_null = pd.read_sql_query(query2,mydb)
columns1 = ['action','description']
trainSet = custom_training
testSet = action_null[columns1]

print(trainSet.head())
print(testSet.head())

# Get Distinct Values of Actions Field with Index Number 
path1 = "C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\distinct-case-actions.txt"
distinct_actions = pd.read_csv(path1)
print(distinct_actions.head())

#merge training set with distinct-case-actions.txt to get the index value for distinct actions 
trainSet = trainSet.merge(distinct_actions, on='action')
print(trainSet.head())

r = re.compile(r'[^\w\s]+')

testSet['description'] = [r.sub('', x) for x in testSet['description'].tolist()]
testSet['description'] = testSet['description'].str.lower().str.split()
print(testSet.head())

stopwords = stopwords.words('english')
#remove stopwords in trainSet 
# trainSet['description'] = trainSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
# print("stopwords")
# print(trainSet.head())
# print()

#remove stopwords in testSet 
testSet['description'] = testSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
print(testSet.head())

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

#join back 
# trainSet1['description'] = trainSet1 ['description'].apply(lambda x:' '.join(x))
#testSet['description'] = testSet['description'].apply(lambda x:[item for item in x if len(x) < 7])
testSet['description'] = testSet['description'].apply(lambda x:' '.join(x))
# print()

# trainSet1['description'] = trainSet1['description'].astype('str')
testSet['description'] = testSet['description'].astype('str')

tags = ["IN", "CC", "CD"]
testSet['description'] = testSet['description'].apply(lambda x:[a[0] for a in nltk.pos_tag(word_tokenize(x)) if a[1] not in tags ])
testSet['description'] = testSet['description'].apply(' '.join)
print(testSet.head())

#print("testSet - get rid of wrong words/misspelled words")
#words = set(nltk.corpus.words.words())
#testSet['description'] = testSet['description'].apply(lambda x:[w for w in nltk.wordpunct_tokenize(x) if w.lower() in words or not w.isalpha()  ])
#print(testSet.head())

#testSet['description'] = testSet['description'].apply(' '.join)
#print(testSet.head())

#copy
trainSet1 = copy.deepcopy(trainSet)
testSet1 = copy.deepcopy(testSet)

print("preprocessing done")
print(trainSet1.head())
print(testSet1.head())

path6 = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\preprocessed-test.txt'
testSet1.to_csv(path6, mode='w', index = False)

#train-test-split starts 
#X = trainSet1['description']
X = trainSet1['description']
y = trainSet1['action_index']

print("train-test-split processing")
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)


clf1 = Pipeline([('tfidf', TfidfVectorizer()),('rdf',RandomForestClassifier()),])
# training data through the pipeline
clf1.fit(X_train, y_train)

#RandomForest Prediction 
prediction1 = clf1.predict(testSet1['description'])
#prediction1 = clf1.predict(testSet1['preprocessed_desc'])
print(prediction1.shape)
print(prediction1)
print() 

print('RF accuracy score')
print(accuracy_score(y_test, prediction1))
print('Mean Squared accuracy score')
print(mean_squared_error(y_test, prediction1))
print("RMSE on testing set = ", math.sqrt(mean_squared_error(y_test, prediction1)))

print ('RF accuracy: TRAINING', clf1.score(X_train,y_train))
print ('RF accuracy: TESTING', clf1.score(X_test,y_test))

clf2 = Pipeline([('tfidf', TfidfVectorizer()),('mnb',MultinomialNB()),])
# training data through the pipeline
clf2.fit(X_train, y_train)

#MultinomialNB Prediction 
prediction2 = clf2.predict(testSet1['description'])
#prediction2 = clf2.predict(testSet1['preprocessed_desc'])
print(prediction2.shape)

print('MNB accuracy score')
print(accuracy_score(y_test, prediction2))
print ('MNB accuracy: TRAINING', clf2.score(X_train,y_train))
print ('MNB accuracy: TESTING', clf2.score(X_test,y_test))


clf3 = Pipeline([('tfidf', TfidfVectorizer()),('lsvc', LinearSVC(dual=False,C = 0.2)),])
# training data through the pipeline
clf3.fit(X_train, y_train)

#LinearSVC Prediction 
prediction3 = clf3.predict(testSet1['description'])
#prediction3 = clf3.predict(testSet1['preprocessed_desc'])
print(prediction3.shape)

print('LinearSVC accuracy score')
print(accuracy_score(y_test, prediction3))
#score: 

# estimators=[('RDF',clf1),('MNB',clf2),('SVC',clf3)]
# ensemble = VotingClassifier(estimators, voting='hard')
# #fit model to training data
# ensemble.fit(X_train, y_train)

# prediction4 = ensemble.predict(testSet1['description'])
# print(prediction4.shape)

# print(accuracy_score(y_test, prediction4[:9190]))

submission1 = pd.DataFrame({'description':testSet1['description'],'action_index':prediction1})
# #Visualize the first 5 rows
print("prediction 1")
print(submission1.head())
submission1 = submission1.merge(distinct_actions, on='action_index') 
query3 = '''SELECT c.action, c.description as preprocessed_desc FROM wp_courtdocs_NORMALIZED.distinct_case_actions as c;'''
preprocessed_actions = pd.read_sql_query(query3,mydb)
submission1 = submission1.merge(distinct_actions, on='action_index') 
#submission1 = submission1.merge(preprocessed_actions, on='action') 

submission2 = pd.DataFrame({'description':testSet1['description'],'action_index':prediction2})
print("prediction 2")
print(submission2.head())
submission2 = submission2.merge(distinct_actions, on='action_index') 
#submission1 = submission1.merge(preprocessed_actions, on='action') 

path4 = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\RandomForest-Prediction.txt'
path5 = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\MultinomialNB-Prediction.txt'
submission1.to_csv(path4, mode='w', index = False)
submission2.to_csv(path5, mode='w', index = False)
# #testSet1.to_csv(path3, mode='w', index = False, header = False)

