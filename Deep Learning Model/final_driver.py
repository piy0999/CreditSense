import pandas as pd
import numpy as np 
import datetime
import sklearn

import matplotlib.pyplot as plt 

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc,confusion_matrix
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

from sklearn_pandas import DataFrameWrapper

input_file = 'lending-club-data.csv'

process_file = pd.read_csv(input_file, infer_datetime_format=True, encoding="ISO-8859-1", error_bad_lines=False, index_col=False, low_memory=False)

#Undergoing Feature Engineering 

#Selecting features that primarily affect our end result  

features = ['revol_util', 'pub_rec_zero', 'pub_rec', 'open_acc', 'last_major_derog_none', 'last_delinq_none', 'grade', 'sub_grade_num', 'short_emp', 'emp_length_num', 'home_ownership', 'dti', 'purpose', 'inq_last_6mths', ]