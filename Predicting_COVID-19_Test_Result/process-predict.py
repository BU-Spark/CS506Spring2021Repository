import time
import os
import glob
import pandas as pd
import numpy as np
import missingno as msno
from scipy.sparse.construct import random
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2, mutual_info_classif
from imblearn.under_sampling import OneSidedSelection
from imblearn.under_sampling import NeighbourhoodCleaningRule
from imblearn.over_sampling import SMOTEN
from collections import Counter
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from pprint import pprint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import xgboost as xgb
from sklearn.metrics import mean_squared_error, confusion_matrix, f1_score, precision_score, recall_score, plot_roc_curve
from datetime import datetime

# Output file location
wdir = "./output/dict_log.txt"


# Setting Random Seed
seed = 0


# Concatenating Subsets
print("Concatenating subsets...")
path = r'./data/carbon'
all_files = glob.glob(os.path.join(path, "*.csv"))
concat_df = pd.concat((pd.read_csv(f) for f in all_files))
concat_df.to_csv('./data/raw_concatenated.csv', index=False)


# Loading
print("Loading data...")
raw_df = pd.read_csv("./data/raw_concatenated.csv")


# Analyzing NA Distribution & Count NAs
print("Analyzing NA values distribution...")
na_chart = msno.matrix(raw_df)
na_chart_copy = na_chart.get_figure()
na_chart_copy.savefig('output/na_chart.png', bbox_inches = 'tight')
plt.close()
# print(raw_df.shape)
# print(raw_df.isnull().sum())


# Subsetting Columns
print("Dropping unnecessary columns...")
raw_df = raw_df.drop(columns=['batch_date', 'swab_type', 'test_name', 'temperature', 'pulse', 'sys', 'dia', 'rr', 'sats', 'rapid_flu_results', 'rapid_strep_results',
'ctab', 'labored_respiration', 'rhonchi', 'wheezes', 'days_since_symptom_onset', 'cough_severity', 'sob_severity', 'cxr_findings', 'cxr_impression', 
'cxr_label', 'cxr_link', 'er_referral'])


# Age to Categorical
print("Converting Age to binary...")
raw_df['age_greater_than_60'] = np.where(raw_df['age'] > 60, 1, 0)
raw_df = raw_df.drop(columns=['age'])


# Converting objects to strings & Lowercasing
print("Converting to strings & lowercasing...")
# string_col_list = raw_df.drop(columns=['age']).columns
string_col_list = raw_df.columns
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
# print("Checking outlier and scaling on Age")
# raw_df.loc[raw_df['age'] < 150]
# min_max_scaler = MinMaxScaler()
# raw_df['age'] = min_max_scaler.fit_transform(raw_df[['age']])
# # use double brackets to get a df format instead of series. This way scalers will work


# Dropping All Remaining NA
print("Creating full set for non-XGBoost methods...")
raw_df_full = raw_df.drop(columns=['high_risk_interactions'])
# raw_df = raw_df.replace({'None': np.nan, 'Other': np.nan})
raw_df_full.dropna(inplace=True)
string_col_list_1 = raw_df.drop(columns=['high_risk_interactions']).columns
raw_df_full[string_col_list_1] = raw_df_full[string_col_list_1].astype(int)
# raw_df_full[string_col_list_1] = raw_df_full[string_col_list_1].astype("category")
# raw_df_full[string_col_list_1] = pd.to_numeric(raw_df_full[string_col_list_1], downcast='int')
# if you already have numeric dtypes (int8|16|32|64,float64,boolean), then you can use astype(int)
# astype(int) doesn't handle string/objects. In that case, use to_numeric() instead


# Analyzing Distribution of Class Labels
print("Analyzing distribution of class labels...")
#print(raw_df_full['covid19_test_results'].value_counts())
test_histo = raw_df_full['covid19_test_results'].hist()
test_histo_copy = test_histo.get_figure()
test_histo_copy.savefig('output/test_histo.png', bbox_inches = 'tight')
plt.close()


# Train/Validation Split
print("Train/Validation Split...")
# X_train_boost, X_validation_boost, y_train_boost, y_validation_boost = train_test_split(raw_df.drop(['covid19_test_results'], axis=1), 
# raw_df['covid19_test_results'], test_size=0.20, random_state=seed, stratify=raw_df['covid19_test_results'])
X_train_full, X_validation_full, y_train_full, y_validation_full = train_test_split(raw_df_full.drop(['covid19_test_results'], axis=1), 
raw_df_full['covid19_test_results'], test_size=0.2, random_state=seed, stratify=raw_df_full['covid19_test_results'])


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
		print('Feature %d: %f' % (i, fs_chi2.scores_[i]))
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
def chi2_select_no_graph():
	fs_chi2 = select_features_chi2_helper(X_train_full, y_train_full)
	chi2_dict = {}
	for i in range(len(fs_chi2.scores_)):
		chi2_dict[i] = fs_chi2.scores_[i]
	chi2_dict = sorted(chi2_dict, key=chi2_dict.get, reverse = True)
	return chi2_dict
def mi_select_no_graph():
	fs_mi = select_features_mi_helper(X_train_full, y_train_full)
	mi_dict = {}
	for i in range(len(fs_mi.scores_)):
		mi_dict[i] = fs_mi.scores_[i]
	mi_dict = sorted(mi_dict, key=mi_dict.get, reverse = True)
	return mi_dict
# two calls below are only used to create graphs. Actual repeated checking is done below
chi2_dict = chi2_select()
mi_dict = mi_select()
# feature_set = set(mi_select_no_graph()[:17])
# temp_set = set(chi2_select_no_graph()[:14])
# feature_set = feature_set.union(temp_set)
# for rep_mi in range(17, 7, -1):
#     temp_feature_set = set(mi_select_no_graph()[:rep_mi])
#     feature_set.intersection_update(temp_feature_set)
# print(feature_set)
feature_set = [9, 10, 14, 15, 16, 18]
# ['high_risk_exposure_occupation', 'diabetes', 'chd', 'htn', 'cancer',
#        'asthma', 'copd', 'autoimmune_dis', 'smoker', 'cough', 'fever', 'sob',
#        'diarrhea', 'fatigue', 'headache', 'loss_of_smell', 'loss_of_taste',
#        'runny_nose', 'muscle_sore', 'sore_throat', 'age_greater_than_60']
X_train_full_colnames = X_train_full.columns
fs_colnames = []
for elem in feature_set:
    fs_colnames.append(X_train_full_colnames[elem])
X_train_full_fs = X_train_full[fs_colnames]
X_validation_full_fs = X_validation_full[fs_colnames]
print(X_train_full_fs.columns)
# can't use SelectKBest to transform, because you still want column names. SelectKBest returns a np array,
# and transforming to pandas requires you to specify column names. You don't know which ones are which 
# unless you manually look
# fs_post = SelectKBest(score_func=mutual_info_classif, k='13')
# fs_post.fit(X_train_full, y_train_full)
# X_train_fs_post = fs_post.transform(X_train_full)
# X_validation_fs_post = fs_post.transform(X_validation_full)
# X_train_fs_post = pd.DataFrame(X_train_fs_post, columns = X_train_full.columns)
# X_validation_fs_post = pd.DataFrame(X_validation_fs_post, columns = X_train_full.columns)


# # One-Class Classification
# clf = IsolationForest(n_estimators=500, max_features=6, bootstrap=True, n_jobs=-1, random_state=0, warm_start=True).fit(X_train_full_fs)
# y_pred = clf.predict(X_validation_full_fs)
# for hhh in range(len(y_pred)):
#     if y_pred[hhh] == 1:
#         y_pred[hhh] = 0
#     else:
#         y_pred[hhh] = 1
# my_f1 = f1_score(y_validation_full, y_pred, average='macro')
# print("f1_macro for Isolation Forest Classifier = ", my_f1)
# cm = confusion_matrix(y_validation_full, y_pred, normalize='true')
# sns.heatmap(cm, annot=True)
# plt.title('Confusion matrix of the Isolation Forest classifier')
# plt.xlabel('Predicted')
# plt.ylabel('True')
# plt.savefig('./output/Random_Forest.png')
# plt.show()


# Oversampling by SMOTEN (Variant of SMOTE on categorical, using VDM)
print("Oversampling...")
counter = Counter(y_train_full)
print("Before oversampling, the class distribution is:")
print(counter)
class_dist = y_train_full.value_counts()
desired_ratio = {0: class_dist[0], 1: class_dist[0]//5}
oversample_smoten = SMOTEN(sampling_strategy=desired_ratio, random_state=seed, n_jobs=-1)
X_train_full_fs, y_train_full = oversample_smoten.fit_resample(X_train_full_fs, y_train_full)
counter = Counter(y_train_full)
print("After oversampling, the class distribution is:")
print(counter)


# Undersample with One-Sided Selection (Tomek Links + Condensed Nearest Neighbor)
print("Undersampling...")
# n_seeds_S is the number of majority class to be added to set C, which is then used as a reference for a kNN on the remaining majority samples not in set C
undersample_oss = OneSidedSelection(n_neighbors=1, n_seeds_S=counter[1], n_jobs=-1, random_state=seed)
X_train_full_fs, y_train_full = undersample_oss.fit_resample(X_train_full_fs, y_train_full)
counter = Counter(y_train_full)
print("After OSS undersampling, the class distribution is:")
print(counter)
undersample_ncr = NeighbourhoodCleaningRule(n_neighbors=3, threshold_cleaning=0.5, n_jobs=-1)
X_train_full_fs, y_train_full = undersample_ncr.fit_resample(X_train_full_fs, y_train_full)
counter = Counter(y_train_full)
print("After NCR undersampling, the class distribution is:")
print(counter)


# Saving to Local
print("Saving to Local in csv...")
X_train_full_fs.to_csv("./data/X_train.csv", index=False)
X_validation_full_fs.to_csv("./data/X_validation.csv", index=False)
y_train_full.to_csv("./data/Y_train.csv", index=False)
y_validation_full.to_csv("./data/Y_validation.csv", index=False)


# Read from Local
print("Reading from local...")
X_train_full_fs = pd.read_csv("./data/X_train.csv")
X_validation_full_fs = pd.read_csv("./data/X_validation.csv")
y_train_full = pd.read_csv("./data/Y_train.csv")
y_validation_full = pd.read_csv("./data/Y_validation.csv")
X_train_full_fs = X_train_full_fs.astype(int)
X_validation_full_fs = X_validation_full_fs.astype(int)
y_train_full = y_train_full.astype(int)
y_validation_full = y_validation_full.astype(int)


# Spot Checking
train_temp = X_train_full_fs
train_temp['target'] = y_train_full
X_train_temp, X_validation_temp, y_train_temp, y_validation_temp = train_test_split(train_temp.drop(['target'], axis=1), 
train_temp['target'], test_size=0.2, random_state=seed, stratify=train_temp['target'])
# KNN
print("Running Models...")
def knn(train_x, train_y, test_x, test_y):
    neigh = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
    neigh.fit(train_x, train_y)
    y_predictions = neigh.predict(test_x)
    print("RMSE for KNN model = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for kNN Classifer = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the KNN classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/KNN.png')
    plt.show()
print("KNN...")
knn(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)

# Logistic
def log(train_x, train_y, test_x, test_y):
    logi = LogisticRegression(n_jobs=-1)
    logi.fit(train_x, train_y)
    y_predictions = logi.predict(test_x)
    print("RMSE for Logistic model = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for Logistic Classifier = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Logistic classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/Logistic.png')
    plt.show()
print("LR...")
log(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)

# Decision Tree
def dectree(train_x, train_y, test_x, test_y):
    dect = DecisionTreeClassifier()
    dect.fit(train_x, train_y)
    y_predictions = dect.predict(test_x)
    print("RMSE for Decision Tree model = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for Decision Tree = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Decision Tree classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/Decision_Tree.png')
    plt.show()
print("DT...")   
dectree(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)

# Complement Naive Bayes
def cnb(train_x, train_y, test_x, test_y):
    compnb =  CategoricalNB()
    compnb.fit(train_x, train_y)
    y_predictions = compnb.predict(test_x)
    print("RMSE for Complement Naive Bayes model = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for Categorical Naive Bayes Classifier = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Categorical Naive Bayes classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/CompNB.png')
    plt.show()
print("CNB..") 
cnb(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)

def rfc(train_x, train_y, test_x, test_y):
    rforest = RandomForestClassifier(n_jobs=-1)
    rforest.fit(train_x, train_y)
    y_predictions = rforest.predict(test_x)
    print("RMSE for Random Forest Classifier = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for Random Forest Classifier = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Random Forest classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/Random_Forest.png')
    plt.show()
print("RFC...")
rfc(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)

def xgboo(train_x, train_y, test_x, test_y):
    xgb_model = xgb.XGBClassifier()
    xgb_model.fit(train_x, train_y)
    y_predictions = xgb_model.predict(test_x)
    print("RMSE for XGBoost Classifier = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions)
    print("f1_macro for XGBoost = ", my_f1)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the XGBoost classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/xgboost.png')
    plt.show()
print("XGBoost...")
xgboo(X_train_temp, y_train_temp, X_validation_temp, y_validation_temp)


# Helper Function for Saving Parameters to Local
def dict_to_txt(payload, title, wodir = wdir):
    def add_txt_to_file(filename, content):
        res = open(filename, "a")
        for i in content:
            res.write(str(i))
            res.write("\n")
        res.close()
    #generate payload list
    res = []
    res.append("##########" + title + "##########")
    t1 = str(datetime.now())
    res.append("Report Created: " + t1)
    res.append("\n")
    #loop through the dict
    for key in payload:
        stro = str(key) + " : " + str(payload[key])
        res.append(stro)
    res.append("#"*(len(title)+20))
    #write file
    add_txt_to_file(wodir, res)


# Random Forest Random Search CV
print("RF Random Search CV...")
rf_model = RandomForestClassifier()
# repeated KFold repeats a single KFold process for n_repeats number of times
# on each repeat, the KFolds are partitioned randomly 
rf_cv = RepeatedStratifiedKFold(n_splits=4, n_repeats=3, random_state=seed)
# space defines the search space of your hyperparameters of interest
rf_space = dict()
# whatever you're interested in tuning, add it to the search space as a dictionary item
rf_space['n_estimators'] = [int(x) for x in np.linspace(start = 200, stop = 1500, num = 10)]
rf_space['max_features'] = ['auto', 'sqrt']
my_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
my_depth.append(None)
rf_space['max_depth'] = my_depth
rf_space['min_samples_split'] = [2, 5, 10]
rf_space['min_samples_leaf'] = [1, 2, 4]
rf_space['bootstrap'] = [True, False]
rf_space['n_jobs'] = [-1]
rf_space['class_weight'] = ['balanced']
# a total of 4320 settings, calculated by multiplying the number of elements in each of the parameters
pprint(rf_space)
# define a scoring that suits the problem of interest
# randomized search CV runs for n_iter number of times, each time with a set of parameters randomly picked from the search space defined earlier
# (or that the set of parameter setting tried by the algorithm is given by n_iter). Each set of parameters is a random sample from the grid/search space
# since we're ysing repeated k folds, each set of parameters is cross validated for n_repeats number of times (defined in cv), and each time it is
# a KFold cross validation
rf_search = RandomizedSearchCV(estimator=rf_model, param_distributions=rf_space, n_iter=2000, scoring='recall_macro', n_jobs=-1, cv=rf_cv, random_state=seed)
# after everything is defined, fit the random search CV to training data to initiate the random search cv process
# the output would 
s_time = time.perf_counter()
rf_result = rf_search.fit(X_train_full_fs, y_train_full.values.ravel())
f_time = time.perf_counter()
print('random search took: ' + str(f_time - s_time) + ' seconds')
print('Best Score: %s' % rf_result.best_score_)
print('Best Hyperparameters: %s' % rf_result.best_params_)
# code be prints the parameters currently in use by a model
# print('Parameters currently in use:\n')
# pprint(rf.get_params())
dict_to_txt(rf_result.best_params_, "rf_best_params")


# Grid Search CV
print("Concentrated Grid Search CV from Random Search CV results...")
# Set up Grid Search CV parameters by expanding in, both directions, the best parameter settings obtained in random search cv
# e.g. best min_sample_leaf values is 4, check 3 and 5 in grid search
# grid search searches every possible combination of parameter values that you specified
rf_model = RandomForestClassifier()
# repeated KFold repeats a single KFold process for n_repeats number of times
# on each repeat, the KFolds are partitioned randomly 
rf_cv = RepeatedStratifiedKFold(n_splits=4, n_repeats=3, random_state=seed)
grid_space = {}
grid_space['n_estimators'] = [922]
grid_space['max_features'] = ['auto']
grid_space['max_depth'] = [9, 10, 11]
grid_space['min_samples_split'] = [4, 5, 6]
grid_space['min_samples_leaf'] = [1, 2]
grid_space['bootstrap'] = [True]
grid_space['n_jobs'] = [-1]
grid_space['class_weight'] = ['balanced']
grid_search = GridSearchCV(estimator=rf_model, param_grid=grid_space, scoring='recall_macro', n_jobs=-1, cv=rf_cv)
grid_result = grid_search.fit(X_train_full_fs, y_train_full)
print('Best Score: %s' % grid_result.best_score_)
print('Best Hyperparameters: %s' % grid_result.best_params_)
best_params = grid_result.best_params_
dict_to_txt(grid_result.best_params_, "grid_rf_best_params")


# Generate model based on best hyperparameters
def rfc(train_x, train_y, test_x, test_y):
    rforest = RandomForestClassifier(n_jobs=-1, n_estimators=922, min_samples_split=5, min_samples_leaf=1, max_features='auto', max_depth=10, 
    bootstrap=True, class_weight='balanced')
    rforest.fit(train_x, train_y)
    y_predictions = rforest.predict(test_x)
    print("RMSE for Random Forest Classifier = ", mean_squared_error(test_y, y_predictions))
    my_f1 = f1_score(test_y, y_predictions, average='macro')
    print("f1_macro for Random Forest Classifier = ", my_f1)
    rec_score = recall_score(test_y, y_predictions, average='macro')
    print("recall_macro for Random Forest Classifier = ", rec_score)
    cm = confusion_matrix(test_y, y_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the Random Forest classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig('./output/rf_final.png')
    plt.show()
    plt.close()
    myroc = plot_roc_curve(rforest, test_x, test_y)
    plt.savefig('./output/rf_final_roc.png')
    plt.show()
print("RFC...")
rfc(X_train_full_fs, y_train_full, X_validation_full_fs, y_validation_full)