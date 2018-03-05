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
from sklearn_pandas import DataFrameMapper
import joblib

INPUT_FILE='lending-club-data.csv'

features = [
    'grade',                 # grade of the loan (categorical)
    'sub_grade_num',         # sub-grade of the loan as a number from 0 to 1
    'short_emp',             # one year or less of employment
    'emp_length_num',        # number of years of employment
    'home_ownership',        # home_ownership status: own, mortgage or rent
    'dti',                   # debt to income ratio
    'purpose',               # the purpose of the loan
    'payment_inc_ratio',     # ratio of the monthly payment to income
    'delinq_2yrs',           # number of delinquincies
    'delinq_2yrs_zero',      # no delinquincies in last 2 years
    'inq_last_6mths',        # number of creditor inquiries in last 6 months
    'last_delinq_none',      # has borrower had a delinquincy
    'last_major_derog_none', # has borrower had 90 day or worse rating
    'open_acc',              # number of open credit accounts
    'pub_rec',               # number of derogatory public records
    'pub_rec_zero',          # no derogatory public records
    'revol_util',            # percent of available credit being used
]
response = 'bad_loans'

numerical_cols=['sub_grade_num', 'short_emp', 'emp_length_num','dti', 'payment_inc_ratio', 'delinq_2yrs', \
                'delinq_2yrs_zero', 'inq_last_6mths', 'last_delinq_none', 'last_major_derog_none', 'open_acc',\
                'pub_rec', 'pub_rec_zero','revol_util']

categorical_cols=['grade', 'home_ownership', 'purpose']

def make_mapper():
    return DataFrameMapper([
        ('grade',sklearn.preprocessing.LabelBinarizer()),
        ('home_ownership', sklearn.preprocessing.LabelBinarizer()),
        ('purpose', sklearn.preprocessing.LabelBinarizer()),
    ])

def train():
    print("reading the input file")
    loans = pd.read_csv(INPUT_FILE, infer_datetime_format=True)
    clean_data=loans[features+[response]].dropna()

    print("transforming the data")
    mapper = make_mapper()
    X1 = mapper.fit_transform(clean_data)
    X2 = np.array(clean_data[numerical_cols])
    X = np.hstack((X1,X2)) #Combines X1 and X2 side by side, i.e. stacks them horizontally
    y = np.array(clean_data['bad_loans'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100, stratify=y)

    print("building the model")
    log_lm = LogisticRegression()
    log_lm.fit(X_train, y_train)
    test_score = log_lm.score(X_test, y_test)
    print(test_score)

    print("saving the model")
    joblib.dump(mapper, "mapper.pkl")
    joblib.dump(log_lm, "logistic-regression-model.pkl")

_mapper = None
_model = None

def load_mapper():
    global _mapper
    if _mapper is None:
        _mapper = joblib.load("mapper.pkl")
    return _mapper

def load_model():
    global _model
    if _model is None:
        _model = joblib.load("logistic-regression-model.pkl")
    return _model

def preprocess(mapper, row):
    data=list(row.values())
    colz=list(row.keys())
    dfx=pd.DataFrame(data=[data], columns=colz)

    XX1=mapper.transform(dfx)
    XX2=dfx[numerical_cols]
    XX = np.hstack((XX1,XX2))
    return XX

def predict(row):
    mapper = load_mapper()
    model = load_model()

    row = preprocess(mapper, row)
    try:
        return model.predict_proba(row)[:,1][0]
    except:
        return -1

if __name__ == '__main__':
    train()