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
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PolynomialFeatures
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

import mysql.connector

mydb = mysql.connector.connect(host='73.38.248.152', user='buspark', password='U@5p1r3!')

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

#distinct values
df = pd.read_csv('./Civera/Data/distinct-case-actions.csv', index_col=int)
print(df.head())


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

# text_clf2 = Pipeline([('tfidf', TfidfVectorizer()),
#                      ('rdf',RandomForestClassifier()),
# ])
# # Feed the training data through the pipeline
# text_clf2.fit(X_train[:10000], y_train[:10000])


#Preparing data
X_train, X_test, Y_train, Y_test = train_test_split(
        trainSet1['actor','description'],
        trainSet1['action'],
        test_size=1
    )

# # Process the DataFrames
# # This is where you can do more feature extraction
# #X_train_processed = X_train.drop(columns=['Id', 'Text', 'ProductId', 'UserId'])
# #X_test_processed = X_test.drop(columns=['Id', 'Text', 'ProductId', 'UserId'])
# # X_submission_processed = X_submission.drop(columns=['Id', 'Text', 'ProductId', 'UserId', 'Score'])

# # I tried to add some interaction terms - then SVD takes a bit longer
# poly = PolynomialFeatures(interaction_only=True, include_bias = False).fit(X_train_processed)
# X_train_processed = poly.transform(X_train_processed)
# X_test_processed = poly.transform(X_test_processed)
# X_submission_processed = poly.transform(X_submission_processed)

# # Scales the data to the (0, 1) range
# # You can also use StandarScalar
# scaler = MinMaxScaler().fit(X_train_processed)
# X_train_processed = scaler.transform(X_train_processed)
# X_test_processed = scaler.transform(X_test_processed)
# X_submission_processed = scaler.transform(X_submission_processed)

# # Visualize the singular value plot
# # u,s,vt=np.linalg.svd(X_train_processed,full_matrices=False)
# # _ = plt.plot(s)
# # plt.title('Singular values of X_train')
# # # plt.show()

# # Pick N_COMPONENTS based on above plot
# pca = PCA(n_components=N_COMPONENTS).fit(X_train_processed)
# X_train_processed = pca.transform(X_train_processed)
# X_test_processed = pca.transform(X_test_processed)
# X_submission_processed = pca.transform(X_submission_processed)

# # Trying to set class weights manually
# class_weight = {1.0: 1.5, 2.0: 3.0, 3.0: 2.5, 4.0: 1.5, 5.0: 0.5}

# # Learn the model
# # Note: I experimented with a few penalty / solvers
# lr = LogisticRegression(penalty='l1', verbose=2, solver='saga', max_iter=300, class_weight=class_weight)

# # Boost the model
# # Note: it took too much time to run so I didn't use it
# # bagging = AdaBoostClassifier(lr, n_estimators=30, n_jobs=3)

# model = lr.fit(X_train_processed, Y_train)

# # Predict the score using the model
# Y_test_predictions = model.predict(X_test_processed)
# X_submission['Score'] = model.predict(X_submission_processed)

# # Evaluate your model on the testing set
# print("RMSE on testing set = ", math.sqrt(mean_squared_error(Y_test, Y_test_predictions)))

# # Plot a confusion matrix
# cm = confusion_matrix(Y_test, Y_test_predictions, normalize='true')
# sns.heatmap(cm, annot=True)
# plt.title('Confusion matrix of the classifier')
# plt.xlabel('Predicted')
# plt.ylabel('True')
# plt.show()

# # Note: based on the confusion matrix you could
# # play around with the weights

# # Create the submission file
# submission = X_submission[['Id', 'Score']]
# submission.to_csv("./data/submission.csv", index=False)