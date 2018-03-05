import pandas as pd, numpy as np
import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.model_selection import GridSearchCV

import sklearn
import requests
import json
from sklearn_pandas import DataFrameMapper

import csv
import matplotlib.pyplot as plt

input_file='lending-club-data.csv'
loan_file = pd.read_csv(input_file, infer_datetime_format = True, encoding = "ISO-8859-1", error_bad_lines=False, index_col=False, low_memory=False)

f = open('id.txt','r')
message = f.read()

message = int(message)

df = loan_file.loc[loan_file['member_id'] == message]

features = ['grade',                     # grade of the loan (categorical)
            'sub_grade_num',             # sub-grade of the loan as a number from 0 to 1
            'short_emp',                 # one year or less of employment
            'emp_length_num',            # number of years of employment
            'home_ownership',            # home_ownership status: own, mortgage or rent
            'dti',                       # debt to income ratio
            'purpose',                   # the purpose of the loan
            'payment_inc_ratio',         # ratio of the monthly payment to income
            'delinq_2yrs',               # number of delinquincies 
            'delinq_2yrs_zero',          # no delinquincies in last 2 years
            'inq_last_6mths',            # number of creditor inquiries in last 6 months
            'last_delinq_none',          # has borrower had a delinquincy
            'last_major_derog_none',     # has borrower had 90 day or worse rating
            'open_acc',                  # number of open credit accounts
            'pub_rec',                   # number of derogatory public records
            'pub_rec_zero',              # no derogatory public records
            'revol_util',                # percent of available credit being used
           ]

response='bad_loans'

clean_data=loan_file[features+[response]].dropna()

parameter_cols=['sub_grade_num', 'short_emp', 'emp_length_num','dti', 'payment_inc_ratio', 'delinq_2yrs',
                'delinq_2yrs_zero', 'inq_last_6mths', 'last_delinq_none', 'last_major_derog_none', 'open_acc',
                'pub_rec', 'pub_rec_zero','revol_util']

categorical_cols=['grade', 'home_ownership', 'purpose']

mapper = DataFrameMapper([
('grade',sklearn.preprocessing.LabelBinarizer()),
('home_ownership', sklearn.preprocessing.LabelBinarizer()),
('purpose', sklearn.preprocessing.LabelBinarizer()),
        
    ])

X1=mapper.fit_transform(clean_data)


X2=np.array(clean_data[parameter_cols])


X = np.hstack((X1,X2)) #Combines X1 and X2 side by side, i.e. stacks them horizontally
y=np.array(clean_data['bad_loans'])


#Train and split the data 33%

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100, stratify=y)


#Logistic Regression Model

log_lm = LogisticRegression()
log_lm.fit(X_train, y_train)
log_lm.score(X_test, y_test)

#Gradient Boosting Model

grd = GradientBoostingClassifier(n_estimators=100)
grd.fit(X_train, y_train)
grd.score(X_test, y_test)

#Decision Tree Model

dtree=DecisionTreeClassifier()
parameters = {'max_depth':[5, 10, 15, 20, 25, 32]}
dtree_gs = GridSearchCV(dtree, parameters, cv=5)
dtree_gs.fit(X_train, y_train)
dtree_gs.score(X_test, y_test)

#Random Tree Model

rf=RandomForestClassifier()
parameters = {'max_depth':[5, 15], 'n_estimators':[10,30]}
rf_gs = GridSearchCV(rf, parameters)
rf_gs.fit(X_train, y_train)
rf_gs.score(X_test, y_test)


#Running a sample data set to process a loan application  one at a time

def preProcess(a):
    data=list(a.values())
    colz=list(a.keys())
    dfx=pd.DataFrame(data=[data], columns=colz)
    dfx

    XX1=mapper.transform(dfx)
    XX2=dfx[parameter_cols]
    XX = np.hstack((XX1,XX2))
    return XX

a={ 'delinq_2yrs': df.delinq_2yrs.item(),
 'delinq_2yrs_zero': df.delinq_2yrs_zero.item(),
 'dti': df.dti.item(),
 'emp_length_num': df.emp_length_num.item(),
 'grade': df.grade.item(),
 'home_ownership': df.home_ownership.item(),
 'inq_last_6mths': df.inq_last_6mths.item(),
 'last_delinq_none': df.last_delinq_none.item(),
 'last_major_derog_none': df.last_major_derog_none.item(),
 'open_acc': df.open_acc.item(),
 'payment_inc_ratio': df.payment_inc_ratio.item(),
 'pub_rec': df.pub_rec.item(),
 'pub_rec_zero': df.pub_rec_zero.item(),
 'purpose': df.purpose.item(),
 'revol_util': df.revol_util.item(),
 'short_emp': df.short_emp.item(),
 'sub_grade_num': df.sub_grade_num.item()}

XX=preProcess(a)

score = log_lm.predict_proba(XX)[:,1][0]

score = score * 10
score = 10 - score
score = str(score)

"""data = [{'Credit Score': score}]
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)"""


#Sending out post
r = requests.post('https://hooks.zapier.com/hooks/catch/2888786/80e87z/', data = {'Credit Score': score})