import pickle

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
import pickle
import matplotlib.pyplot as plt


loaded_model = pickle.load(open('finalized_model.sav', 'rb')) #loading the saved logistic regression model
loaded_mapper = pickle.load(open('mapper.pkl', 'rb')) #loading the saved mapper pickle file

from sklearn_pandas import DataFrameMapper


def preProcess(a, mapper,parameter_cols):
    data=list(a.values())
    colz=list(a.keys())
    dfx=pd.DataFrame(data=[data], columns=colz)
    dfx

    XX1=mapper.transform(dfx)
    XX2=dfx[parameter_cols]
    XX = np.hstack((XX1,XX2))
    return XX


parameter_cols=['sub_grade_num', 'short_emp', 'emp_length_num','dti', 'payment_inc_ratio', 'delinq_2yrs',
                'delinq_2yrs_zero', 'inq_last_6mths', 'last_delinq_none', 'last_major_derog_none', 'open_acc',
                'pub_rec', 'pub_rec_zero','revol_util']

a={ 'delinq_2yrs': "0",
'delinq_2yrs_zero': "1",
'dti': "11.18",
'emp_length_num': "10",
'grade': "B",
'home_ownership': "OWN",
'inq_last_6mths': "0",
'last_delinq_none': "1",
'last_major_derog_none': "1",
'open_acc': "8",
'payment_inc_ratio': "7.93824",
'pub_rec': "0",
'pub_rec_zero': "1",
'purpose': "credit_card",
'revol_util': "82.4",
'short_emp': "0",
'sub_grade_num': "0.6"}

XX=preProcess(a, loaded_mapper,parameter_cols)

score = loaded_model.predict_proba(XX)[:,1][0]

score = score * 10
score = 10 - score
score = str(score)

print("Score: ",score)
