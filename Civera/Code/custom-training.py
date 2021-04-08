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

columns = ['action','description']
custom_training = pd.read_csv("C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\custom-training.txt", error_bad_lines=False)
training = custom_training[columns]
print(training.head())
print(training.shape)

custom_training1 = pd.read_sql("SELECT c_a_index.actor, c_a_index.action, c_a_index.description FROM wp_courtdocs.cdocs_case_action_index as c_a_index where  c_a_index.action = 'Affidavit in support of motion' LIMIT 10;", con = mydb)
training1 = custom_training1[columns]
print(training1.head())
print(training1.shape)

training = training.append(training1, ignore_index=True)

print(training.head())
print(training.shape)
#path = 'C:\\Users\\Serra\\Desktop\\CS506Spring2021Repository\\Civera\\Data\\custom-training.txt'
#training.to_csv(path, mode='a', index = False) 