import swifter
import numpy as np
import pandas as pd
import seaborn as sns
import re
import copy
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, confusion_matrix


import mysql.connector

mydb = mysql.connector.connect(host='', user='', password='')

if (mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

#load sql to dataframe 
case_index_not_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action != ' ' and c_a_index.actor != ' ' and rand() <= .2;", con = mydb)

columns = ['actor','action','description']
trainSet = case_index_not_null[columns]
print(trainSet.head())

# cdocs_case_action_index / actor = null
action_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action = ' ' and c_a_index.actor != ' ' and rand() <= .2;", con = mydb)
testSet = action_null[columns]
print(testSet.head())

# X = trainingSet[['action','description']]
# y = trainingSet['actor']

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

r = re.compile(r'[^\w\s]+')
trainSet['description'] = [r.sub('', x) for x in trainSet['description'].tolist()]
trainSet['description'] = trainSet['description'].str.lower().str.split()
testSet['description'] = [r.sub('', x) for x in testSet['description'].tolist()]
testSet['description'] = testSet['description'].str.lower().str.split()

stopwords = stopwords.words('english')
trainSet['description'] = trainSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
print("stopwords")
print(trainSet.head())
print()
testSet['description'] = testSet['description'].apply(lambda x: [item for item in x if item not in stopwords])
print(testSet.head())


lemmatizer = WordNetLemmatizer() 
trainSet['description'] = trainSet['description'].apply(lambda x:[lemmatizer.lemmatize(word) for word in x])
testSet['description'] = testSet['description'].apply(lambda x:[lemmatizer.lemmatize(word) for word in x])

#remove duplicate words after lemmatizing 
trainSet['description'] = trainSet['description'].apply(lambda x:list(dict.fromkeys(x)))
print()
print('trainingSet after lemmatizer & removing dupes ')
print(trainSet.head())

testSet['description'] = testSet['description'].apply(lambda x:list(dict.fromkeys(x)))
print()
print('testSet after lemmatizer & removing dupes ')
print(testSet.head())

#copy
trainSet1 = copy.deepcopy(trainSet)
testSet1 = copy.deepcopy(testSet)

#join back 
trainSet1['description'] = trainSet1 ['description'].apply(lambda x:' '.join(x))
testSet1['description'] = testSet1['description'].apply(lambda x:' '.join(x))
print()

trainSet1['description'] = trainSet1['description'].astype('str')
testSet1['description'] = testSet1['description'].astype('str')

#trainSet1.to_csv("./Civera/Data/action_train.csv", mode='w', index = False, header = False)
#testSet1.to_csv("./Civera/Data/action_test.csv", mode='w', index = False, header = False)

print("done")