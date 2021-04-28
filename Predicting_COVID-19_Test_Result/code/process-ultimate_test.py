import time
import os
import glob
import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, confusion_matrix
from collections import Counter
from imblearn.under_sampling import OneSidedSelection
from imblearn.under_sampling import NeighbourhoodCleaningRule
import xgboost as xgb



###KNN & Logistic & Complement NB & Decision Tree Testing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.ensemble import RandomForestClassifier

# Concatenating Subsets
# print("Concatenating subsets...")
# path = r'./data/carbon'
# all_files = glob.glob(os.path.join(path, "*.csv"))
# concat_df = pd.concat((pd.read_csv(f) for f in all_files))
# concat_df.to_csv('./data/raw_concatenated.csv', index=False)


# Loading
print("Loading data...")
raw_df = pd.read_csv("./data/raw_concatenated.csv")


# Subsetting Columns
print("Dropping unnecessary columns...")
raw_df = raw_df.drop(columns=['batch_date', 'swab_type', 'test_name', 'temperature', 'pulse', 'sys', 'dia', 'rr', 'sats', 'rapid_flu_results', 'rapid_strep_results',
'ctab', 'labored_respiration', 'rhonchi', 'wheezes', 'days_since_symptom_onset', 'cough_severity', 'sob_severity', 'cxr_findings', 'cxr_impression', 
'cxr_label', 'cxr_link', 'er_referral'])


# Analyzing NA Distribution & Count NAs
print("Analyzing NA values distribution...")
na_chart = msno.matrix(raw_df)
na_chart_copy = na_chart.get_figure()
na_chart_copy.savefig('output/na_chart.png', bbox_inches = 'tight')
plt.close()
# print(raw_df.shape)
# print(raw_df.isnull().sum())


# Converting objects to strings & Lowercasing
print("Converting to strings & lowercasing...")
string_col_list = raw_df.drop(columns=['age']).columns
raw_df[string_col_list] = raw_df[string_col_list].astype(str)
# don't use .apply(str) ever again. It force-applies a string type, which would include the newline character
for string_col in string_col_list:
    raw_df[string_col] = raw_df[string_col].str.lower()


# No NAN Encoding
print("Encoding...")
bool_col_list = ['high_risk_exposure_occupation', 'high_risk_interactions', 'diabetes', 'chd', 'htn', 'cancer', 'asthma', 'copd', 'autoimmune_dis', 
'smoker', 'cough', 'fever', 'sob', 'diarrhea', 'fatigue', 'headache', 'loss_of_smell', 'loss_of_taste', 'runny_nose', 'muscle_sore', 'sore_throat']
raw_df[bool_col_list] = raw_df[bool_col_list].replace({'true': 1, 'false': 0, 'nan': np.nan})
raw_df['covid19_test_results'] = raw_df['covid19_test_results'].replace({'negative': 0, 'positive': 1, 'nan': np.nan})
# bad encoders, need reshaping and doesn't work
# bool_label_encoder = OneHotEncoder(handle_unknown='ignore')
# bool_label_encoder = bool_label_encoder.fit(raw_df['high_risk_exposure_occupation']) 
# # did not use fit_transform() because I want encoding to be memorized/to be able to apply the same encoding for different columns of the same values
# # also good for inverse transform
# bool_col_list = ['high_risk_exposure_occupation', 'high_risk_interactions', 'diabetes', 'chd', 'htn', 'cancer', 'asthma', 'copd', 'autoimmune_dis', 
# 'smoker', 'cough', 'fever', 'sob', 'diarrhea', 'fatigue', 'headache', 'loss_of_smell', 'loss_of_taste', 'runny_nose', 'muscle_sore', 'sore_throat']
# for bool_col in bool_col_list:
#     raw_df[bool_col] = bool_label_encoder.transform(raw_df[bool_col])


# Age Outlier & Scaling
print("Checking outlier and scaling on Age")
raw_df.loc[raw_df['age'] < 150]
min_max_scaler = MinMaxScaler()
raw_df['age'] = min_max_scaler.fit_transform(raw_df[['age']])
# use double brackets to get a df format instead of series. This way scalers will work


# Converting to Categorical
print("Converting to Categorical...")
raw_df[string_col_list] = raw_df[string_col_list].astype("category")


# Dropping All Remaining NA
print("Creating full set for non-XGBoost methods...")
raw_df_full = raw_df.drop(columns=['high_risk_interactions', 'fever'])
# raw_df = raw_df.replace({'None': np.nan, 'Other': np.nan})
raw_df_full.dropna(inplace=True)
string_col_list_1 = raw_df.drop(columns=['age', 'high_risk_interactions', 'fever']).columns
raw_df_full[string_col_list_1] = raw_df_full[string_col_list_1].astype(int)
raw_df_full[string_col_list_1] = raw_df_full[string_col_list_1].astype("category")


# Analyzing Distribution of Class Labels
print("Analyzing distribution of class labels...")
#print(raw_df['covid19_test_results'].value_counts())
test_histo = raw_df['covid19_test_results'].hist()
test_histo_copy = test_histo.get_figure()
test_histo_copy.savefig('output/test_histo.png', bbox_inches = 'tight')
plt.close()


# Train/Validation Split
print("Train/Validation Split...")
X_train_boost, X_validation_boost, y_train_boost, y_validation_boost = train_test_split(raw_df.drop(['covid19_test_results'], axis=1), 
raw_df['covid19_test_results'], test_size=0.20, random_state=0, stratify=raw_df['covid19_test_results'])
X_train_full, X_validation_full, y_train_full, y_validation_full = train_test_split(raw_df_full.drop(['covid19_test_results'], axis=1), 
raw_df_full['covid19_test_results'], test_size=0.20, random_state=0, stratify=raw_df_full['covid19_test_results'])


# Feature Selection
print("Feature selection...")
def select_features_chi2_helper(X_train, y_train):
	fs = SelectKBest(score_func=chi2, k='all')
	fs.fit(X_train, y_train)
	# X_train_fs = fs.transform(X_train)
	# X_validation_fs = fs.transform(X_validation)
    # could have set k to a number, and returned the transformed dataset along with function
    # since we want to know how the values distributes, no need to return the full dataset
	return fs
def select_features_mi_helper(X_train, y_train):
	fs = SelectKBest(score_func=mutual_info_classif, k='all')
	fs.fit(X_train, y_train)
	# X_train_fs = fs.transform(X_train)
	# X_validation_fs = fs.transform(X_validation)
	return fs
def chi2_select():
	fs_chi2 = select_features_chi2_helper(X_train_full, y_train_full)
	chi2_dict = {}
	for i in range(len(fs_chi2.scores_)):
		chi2_dict[i] = fs_chi2.scores_[i]
		# print('Feature %d: %f' % (i, fs_chi2.scores_[i]))
	chi2_dict = sorted(chi2_dict, key=chi2_dict.get, reverse = True)
	plt.bar([i for i in range(len(fs_chi2.scores_))], fs_chi2.scores_)
	plt.savefig('output/chi2_fs.png', bbox_inches = 'tight')
	plt.close()
	# closing the plot works here. plt.clf() throws a Tkinter exception (perhaps due to memory?)
	return chi2_dict
def mi_select():
	fs_mi = select_features_mi_helper(X_train_full, y_train_full)
	mi_dict = {}
	for i in range(len(fs_mi.scores_)):
		mi_dict[i] = fs_mi.scores_[i]
		# print('Feature %d: %f' % (i, fs_mi.scores_[i]))
	mi_dict = sorted(mi_dict, key=mi_dict.get, reverse = True)
	plt.bar([i for i in range(len(fs_mi.scores_))], fs_mi.scores_)
	plt.savefig('output/mi_fs.png', bbox_inches = 'tight')
	plt.close()
	return mi_dict
def mi_select_no_graph():
	fs_mi = select_features_mi_helper(X_train_full, y_train_full)
	mi_dict = {}
	for i in range(len(fs_mi.scores_)):
		mi_dict[i] = fs_mi.scores_[i]
		# print('Feature %d: %f' % (i, fs_mi.scores_[i]))
	mi_dict = sorted(mi_dict, key=mi_dict.get, reverse = True)
	return mi_dict
# two calls below are only used to create graphs. Actual repeated checking is done below
chi2_dict = chi2_select()
mi_dict = mi_select()
# feature_set = set(mi_select_no_graph()[:18])
# for rep_mi in range(17, 10, -1):
# 	if rep_mi < 13:
# 		temp_feature_set = set(mi_select_no_graph()[:13])
# 		feature_set.intersection_update(temp_feature_set)
# 	else:
# 		temp_feature_set = set(mi_select_no_graph()[:rep_mi])
# 		feature_set.intersection_update(temp_feature_set)
feature_set = [0, 10, 13, 14, 15, 16, 18, 19]
X_train_full_colnames = X_train_full.columns
fs_colnames = []
for elem in feature_set:
	fs_colnames.append(X_train_full_colnames[elem])
X_train_full_fs = X_train_full[fs_colnames]
X_validation_full_fs = X_validation_full[fs_colnames]
# can't use SelectKBest to transform, because you still want column names. SelectKBest returns a np array,
# and transforming to pandas requires you to specify column names. You don't know which ones are which 
# unless you manually look
# fs_post = SelectKBest(score_func=mutual_info_classif, k='13')
# fs_post.fit(X_train_full, y_train_full)
# X_train_fs_post = fs_post.transform(X_train_full)
# X_validation_fs_post = fs_post.transform(X_validation_full)
# X_train_fs_post = pd.DataFrame(X_train_fs_post, columns = X_train_full.columns)
# X_validation_fs_post = pd.DataFrame(X_validation_fs_post, columns = X_train_full.columns)


# Undersample with One-Sided Selection (Tomek Links + Condensed Nearest Neighbor)
print("Undersampling...")
# summarize class distribution
counter = Counter(y_train_full)
print(counter)
undersample_oss = OneSidedSelection(n_neighbors=1, n_seeds_S=200)
X_train_full_fs, y_train_full = undersample_oss.fit_resample(X_train_full_fs, y_train_full)
counter = Counter(y_train_full)
print(counter)
undersample_ncr = NeighbourhoodCleaningRule(n_neighbors=3, threshold_cleaning=0.5)
X_train_full_fs, y_train_full = undersample_ncr.fit_resample(X_train_full_fs, y_train_full)
counter = Counter(y_train_full)
print(counter)
print(X_train_full_fs.head())
#X_train_t, X_validation_t, Y_train_t, Y_validation_t = train_test_split(X_train_full_fs, y_train_full, test_size=0.20, random_state=0)


## KNN & Logistic & Random Forest & Complement Naive Bayes & Decision Tree 
# KNN
#X_train_full, X_validation_full, y_train_full, y_validation_full
def knn(train_x, train_y, test_x, test_y):
    neigh = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
    neigh.fit(train_x, train_y)
    y_predictions = neigh.predict(test_x)
    print("RMSE for KNN model = ", mean_squared_error(test_y, y_predictions))
    
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the KNN classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
knn(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)

#logistic
def log(train_x, train_y, test_x, test_y):
    logi = LogisticRegression(n_jobs=-1)
    logi.fit(train_x, train_y)
    y_predictions = logi.predict(test_x)
    print("RMSE for Logistic model = ", mean_squared_error(test_y, y_predictions))
    
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Logistic classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
log(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)


#decision tree
def dectree(train_x, train_y, test_x, test_y):
    logi = DecisionTreeClassifier()
    logi.fit(train_x, train_y)
    y_predictions = logi.predict(test_x)
    print("RMSE for Decision Tree model = ", mean_squared_error(test_y, y_predictions))
    
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Decision Tree classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
dectree(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)

#Complement Naive Bayes
def cnb(train_x, train_y, test_x, test_y):
    logi = ComplementNB(n_jobs=-1)
    logi.fit(train_x, train_y)
    y_predictions = logi.predict(test_x)
    print("RMSE for Complement Naive Bayes model = ", mean_squared_error(test_y, y_predictions))
    
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Complement Naive Bayes classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
cnb(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)


#Random Forest Classifier
def rfc(train_x, train_y, test_x, test_y):
    logi = RandomForestClassifier(n_jobs=-1)
    logi.fit(train_x, train_y)
    y_predictions = logi.predict(test_x)
    print("RMSE for Random Forest Classifier = ", mean_squared_error(test_y, y_predictions))
    
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Random Forest classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
rfc(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)


# # Undersampling

# from sklearn.linear_model import LogisticRegression   
# Lr = LogisticRegression(class_weight='balanced')

'''
# Saving to Local
print("Saving to Local...")
X_train.to_pickle("./data/X_train.pkl")
X_validation.to_pickle("./data/X_validation.pkl")
Y_train.to_pickle("./data/Y_train.pkl")
Y_validation.to_pickle("./data/Y_validation.pkl")
X_submission.to_pickle("./data/X_submission.pkl")
'''

'''
# time
tfidf_s_time = time.perf_counter()
tfidf_f_time = time.perf_counter()
print('tfidf vectorizer took: ' + str(tfidf_f_time - tfidf_s_time) + ' seconds')
'''
