# Need to format Xs and Y
# Going to use just 2017 -- avoid the whole over time dilemma

'''
DEFINE SUCCESS AS >80% of goal reached?
-- go through percent_reached_goal column and generate
new column based on whether it classifies as successful 
'''

'''Attributes: 
-- # Key words in the description --> need to compute based on 'All_Keywords'
-- 'Donors'
-- 'Shares'
-- 'Followers'
-- 'Num_Updates'
-- 'Num_Comments'
-- 'Is_Charity' --> need to encode to 1 or 0 if TRUE or FALSE
-- 'Is_Business' --> need to encode to 1 or 0 if TRUE or FALSE
-- 'Is_Team' --> need to encode to 1 or 0 if TRUE or FALSE
-- 'Description_Length'
-- 'Title_Length'
_________________________sentiment analysis_______________________
Note, to skip a row, they all have to be zero
-- 'Compound_Description'
-- 'Neg_Description'
-- 'Neu_Description'
-- 'Pos_Description'
-- 'Compound_Title'
-- 'Neg_Title'
-- 'Neu_Title'
-- 'Pos_Title' 

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys
import os

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import statsmodels.api as sm

columns = ['Donors','Shares','Followers','Num_Updates','Num_Comments', 'Description_Length', 'Title_Length',
'Compound_Description', 'Neg_Description', 'Neu_Description', 'Pos_Description',
'Compound_Title', 'Neg_Title', 'Neu_Title', 'Pos_Title']

def format_data(data, year, success_metric):
    '''
    Want campaigns from input year (datetime.year)
    Check if campaigns meet a threshold of a certain success and classify as
    1 (success) if they meet that threshold or 0 (not successful) otherwise

    data = pandas dataframe of full dataset, read from a csv
    year = year to focus on (int)
    --(ex. 2017 or 2020)
    success_metric = decimal representing the percent of campaign goal reached (float)
    --(ex. 0.7  or 0.8)

    '''
    # Drop campaigns not in the specified year
    # Format rows as needed to collect proper attributes, predictions
    campaigns_to_drop = []
    success_classifications = []
    num_key_words = []
    TF_dict = {'Is_Charity':[],'Is_Business': [], 'Is_Team':[]}

    for index, row in data.iterrows():
        date_time_obj = datetime.datetime.strptime(row['Campaign_Date'],'%Y-%m-%d %H:%M:%S')
        
        if date_time_obj.year != year:
            campaigns_to_drop.append(index)
        elif pd.isna(row['Donors']) or pd.isna(row['Shares']) or pd.isna(row['Followers']):
            campaigns_to_drop.append(index)
        elif pd.isna(row['Num_Updates']) or pd.isna(row['Num_Comments']):
            campaigns_to_drop.append(index)
        elif row['Percent_Reached'] == np.nan:
            campaigns_to_drop.append(index)
        #when there is no description
        elif row['Compound_Description']==0 and row['Neg_Description']==0 and row['Neu_Description']==0 and row['Pos_Description']==0:
            campaigns_to_drop.append(index)
        
        else: 
            if float(row['Percent_Reached']) >= success_metric:
                success_classifications.append(1)
            else:
                success_classifications.append(0)

            num_key_words.append(len(row['All_Keywords']))

            for attribute in ['Is_Charity','Is_Business','Is_Team']:
                if (row[attribute]) == True:
                    TF_dict[attribute].append(1)
                elif (row[attribute]) == False:
                    TF_dict[attribute].append(0)


    data = pd.DataFrame(data.drop(data.index[campaigns_to_drop]))
    data = data[columns]
    data['Num_Key_Words'] = num_key_words
    data['Success'] = success_classifications
    for key in TF_dict:
        data[key] = TF_dict[key]

    Xs = data.drop(columns=['Success'], axis=1)
    Y = data['Success'].values#.reshape(-1,1)

    print("Total number of successful campagins",np.sum(Y))
    print("Final length of dataset",len(Y))

    return Xs, Y

def reduce_dimensions(Xs):
    '''
    Uses Principle Component Analysis (PCA) to reduce highly correlated
    attributes in Xs
    '''
    from sklearn.decomposition import PCA
    Xs = Xs.drop(columns=['Is_Charity','Is_Business','Is_Team']) #drop attributes deemed irrelevant
    pca = PCA(16).fit(Xs)
    variance_ratios = pca.explained_variance_ratio_.cumsum()

    # plot a line and use the elbow method to determine a proper number to plug into PCA()
    plt.plot([i for i in range(0, 16)], variance_ratios*100)
    plt.axvline(4, c='red') # draw a line at the number of compressed features determined by elbow method
    plt.title("Explained Variance By Principal Components")
    plt.show()

    pca_data = PCA(4).fit_transform(Xs) #transform using PCA
    print(pca_data)

    return pca_data


def print_logit_model(Xs, Y):
    '''
    Computes and prints logit summary to describe how each variable impacts
    the overall success of the model
    '''

    #logit_model = sm.Logit(Y, Xs, missing='drop')
    #result = logit_model.fit()
    #print(result.summary2())
    X2 = sm.add_constant(Xs)
    est = sm.OLS(Y,X2)
    est2 = est.fit()
    print(est2.summary())

    
def create_print_regressor_validated(Xs, Y, n_test):
    """
    Creates a logistic regressor and returns Y_test, Y_pred, X_test
    Also prints the accuracy of the logistic regression and generates an ROC Curve
    
    n_test : float between 0.0-1.0
        Input the proportion of the dataset to include in the test split
    """
    X_train, X_test, Y_train, Y_test = train_test_split(Xs, Y, test_size = n_test, random_state = 0)
    logreg = LogisticRegression()
    logreg.fit(X_train, Y_train)    
    Y_pred = logreg.predict(X_test)
    
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, Y_test)))
    
    return logreg, Y_test, Y_pred, X_test    #don't need Y_train or X_train beyond here

def print_confusion_matrix(y_test, y_pred):
    '''
    Generates a confusion matrix to analyze the performance of the model by
    comparing the y_test set and the predictions y_pred

    also prints the accuracy, sensitivity, and specificity of the model
    '''
    
    confus_matrix = confusion_matrix(y_test, y_pred)
    print(confus_matrix)
    print("correct predictions versus incorrect predictions")
    total1 = sum(sum(confus_matrix))

    accuracy1=(confus_matrix[0,0]+confus_matrix[1,1])/total1
    print ('Accuracy : ', accuracy1)
    
    sensitivity1 = confus_matrix[0,0]/(confus_matrix[0,0]+confus_matrix[0,1])  # proportion of actual positves, predicted correctly
    print('Sensitivity : ', sensitivity1 )
    
    specificity1 = confus_matrix[1,1]/(confus_matrix[1,0]+confus_matrix[1,1])  # proportion of actual negatives, predicted correctly
    print('Specificity : ', specificity1)

def print_diagnostic_abilities(logreg, y_test, y_pred, x_test):
    """
    Prints... 
        ROC curve-- illustrates the diagnostic ability of a binary classifier system 
                as its discrimination threshold is varied. The ROC curve is created by plotting 
                the true positive rate against the false positive rate at various threshold 
                settings.
    """
    
    from sklearn.metrics import roc_auc_score
    from sklearn.metrics import roc_curve
    logit_roc_auc = roc_auc_score(y_test, logreg.predict(x_test))
    fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(x_test)[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.savefig('Log_ROC')
    plt.show() 

def main():
    
    # Navigate from /analysis folder to the parent directory, to access /data folder
    cwd = os.getcwd()
    os.chdir("..")
    
    # Read in most processed file, with sentiment analysis
    data = pd.read_csv('./data/GFM_Data_VADER_Sentiment.csv') 

    # Format the data into Xs (attributes) and Y (whether each campaign was successful)
    Xs,Y = format_data(data, 2020, 0.8)
    #Xs = reduce_dimensions(Xs) #comment out if you want to analyze results of all attributes, uncompressed

    # Print summary of the results from logistic regression, how each variable contributes to the model
    print_logit_model(Xs,Y) 
    
    # Generate logistic regression using a train-test-split validation
    logreg, Y_test, Y_pred, X_test = create_print_regressor_validated(Xs,Y,0.3) 
    print_confusion_matrix(Y_test, Y_pred)
    # print("Confusion matrix key:")
    # cm_key_1 = [['TP','FP']]
    # cm_key_2 = [['FN','TN']]
    # print(cm_key_1,cm_key_2)
    print_diagnostic_abilities(logreg, Y_test, Y_pred, X_test) #plots an ROC Curve
    
def main2():
    '''
    loops through different success thresholds (over 50%) for each year to determine which
    has the highest accuracy, with good sensitivity and specificity as well

    NOT FINISHED
    '''
    data = pd.read_csv('./data/GFM_Data_VADER_Sentiment.csv')
    Xs,Y = format_data(data, 2020)

    success_metrics = [0.5,0.6,0.7,0.8,0.9,1.0]
    #for s in success_metrics:
    #    logreg, Y_test, Y_pred, X_test = create_print_regressor_validated(Xs,Y,0.3)


if __name__ == '__main__':
    main()
