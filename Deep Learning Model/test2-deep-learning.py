import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import sys
sys.version

from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization

from imblearn.over_sampling import SMOTE
from collections import Counter

def drop_null_columns(data):
    data.drop(null_cols, axis=1,inplace= True)
    return 

def split_loan_in_progress(data):
    progress_bool = data.loan_status.isin(in_progress_index)
    loan_in_progress = data[progress_bool].drop('loan_status', axis=1)
    data.drop(list(loan_in_progress.index), axis=0, inplace=True)
    return 

# Returns loan status
def categorize_target(data):
    def func(x):
        if x['loan_status'] in bad_index:
            return 0
        elif x['loan_status'] in warning_index:
            return 1
        else:
            return 2

    data['loan_status_coded'] = data.apply(func, axis=1)
    data.drop('loan_status', axis=1, inplace=True)
    return data

def drop_emp_title(data):
    data.drop('emp_title', axis=1, inplace=True)
    return None

def drop_issue_d(data):
    data.drop('issue_d', axis=1, inplace=True)
    return None


def drop_pymnt_plan(data):
    data.drop('pymnt_plan', axis=1, inplace=True)
    return None


def drop_url(data):
    data.drop('url', axis=1, inplace=True)
    return None

def fill_na_title(data):
    data.title.fillna('Unknown', inplace=True)
    return None

def drop_zip_code(data):
    data.drop('zip_code', axis=1, inplace=True)
    return None

def drop_addr_state(data):
    data.drop('addr_state', axis=1, inplace=True)
    return None

def fill_na_delinq_2yrs(data):
    data.delinq_2yrs.fillna(data.delinq_2yrs.median(), inplace=True)
    return None


def drop_earliest_cr_line(data):
    data.drop('earliest_cr_line', axis=1, inplace=True)
    return None


def fill_na_inq_last_6mths(data):
    data.inq_last_6mths.fillna(data.inq_last_6mths.median(), inplace=True)
    return None

def fill_na_open_acc(data):
    data.open_acc.fillna(data.open_acc.median(), inplace=True)
    return None


def fill_na_pub_rec(data):
    data.pub_rec.fillna(data.pub_rec.median(), inplace=True)
    return None

def fill_na_revol_util(data):
    data.revol_util.fillna(data.revol_util.median(), inplace=True)
    return None


def fill_na_total_acc(data):
    data.total_acc.fillna(data.total_acc.median(), inplace=True)
    return None

def drop_out_prncp(data):
    data.drop('out_prncp', axis=1, inplace=True)
    return None

def drop_out_prncp_inv(data):
    data.drop('out_prncp_inv', axis=1, inplace=True)
    return None


def drop_total_rec_late_fee(data):
    data.drop('total_rec_late_fee', axis=1, inplace=True)
    return None


def drop_recoveries(data):
    data.drop('recoveries', axis=1, inplace=True)
    return None

def drop_collection_recovery_fee(data):
    data.drop('collection_recovery_fee', axis=1, inplace=True)
    return None

def drop_last_pymnt_d(data):
    data.drop('last_pymnt_d', axis=1, inplace=True)
    return None

def drop_last_credit_pull_d(data):
    data.drop('last_credit_pull_d', axis=1, inplace=True)
    return None

def drop_collections_12_mths_ex_med(data):
    data.drop('collections_12_mths_ex_med', axis=1, inplace=True)
    return None

def drop_policy_code(data):
    data.drop('policy_code', axis=1, inplace=True)
    return None

def drop_application_type(data):
    data.drop('application_type', axis=1, inplace=True)
    return None

def drop_acc_now_delinq(data):
    data.drop('acc_now_delinq', axis=1, inplace=True)
    return None

def drop_tot_coll_amt(data):
    data.drop('tot_coll_amt', axis=1, inplace=True)
    return None

def drop_tot_cur_bal(data):
    data.drop('tot_cur_bal', axis=1, inplace=True)
    return None


def fill_na_total_rev_hi_lim(data):
    data.total_rev_hi_lim.fillna(data.total_rev_hi_lim.median(), inplace=True)
    return None

def one_hot_encoder(loan):
    categorical_variables = categorical
    loan_one_hot_encoded = pd.get_dummies(loan, columns=categorical_variables)
    print("====================[Data Types]====================")
    print(loan_one_hot_encoded.dtypes)
    return loan_one_hot_encoded

def encode_neural_net_y(y):
    encoder = LabelEncoder()
    encoder.fit(y)
    encoded_y = encoder.transform(y)
    new_y = np_utils.to_categorical(encoded_y)
    return new_y


#Loading Data into Data Frame
loan = pd.read_csv("loan.csv")

#Dropping NULL columns

null_cols = ['desc',
             'mths_since_last_delinq',
             'mths_since_last_record',
             'next_pymnt_d',
             'mths_since_last_major_derog',
             'annual_inc_joint',
             'dti_joint',
             'verification_status_joint',
             'open_acc_6m',
             'open_il_6m',
             'open_il_12m',
             'open_il_24m',
             'mths_since_rcnt_il',
             'total_bal_il',
             'il_util',
             'open_rv_12m',
             'open_rv_24m',
             'max_bal_bc',
             'all_util',
             'inq_fi',
             'total_cu_tl',
             'inq_last_12m'
             ]

drop_null_columns(loan)

#Splitting Current and Issued loans

in_progress_index = ['Current', 'Issued']

loan_in_progress = split_loan_in_progress(loan)

#categorizing different types of index

bad_index = ['Charged Off',
             'Does not meet the credit policy. Status:Charged Off',
             'Default'
             ]

warning_index = ['Late (31-120 days)',
                 'Late (16-30 days)',
                 'In Grace Period'          # (Late (1-15 days)
                 ]

safe_index = ['Fully Paid',
              'Does not meet the credit policy. Status:Fully Paid'
              ]

loan = categorize_target(loan)

#Drop Employement Title Field
drop_emp_title(loan)

#Drop Issue_D Field
drop_issue_d(loan)

#Drop Payment Plan Field
drop_pymnt_plan(loan)

#Drop URL Field 
drop_url(loan)

#Filling null values with 'Unknown' value
fill_na_title(loan)

#Drop Zip Code Field
drop_zip_code(loan)

#Drop Address State
drop_addr_state(loan)

#Filling NULL delinq_2yrs
fill_na_delinq_2yrs(loan)

#Earliest Credit Line
drop_earliest_cr_line(loan)

#Filling null values with NA
fill_na_inq_last_6mths(loan)

#Filling Null values of empty open accounts
fill_na_open_acc(loan)

#Filling Null values of Public Record
fill_na_pub_rec(loan)

#Filling Null Values of Revol Until
fill_na_revol_util(loan)

#Filling Null of NA total acc
fill_na_total_acc(loan)

#Drop remaining principal 
drop_out_prncp(loan)

#Drop remaining principal portion of investors
drop_out_prncp_inv(loan)

#Drop total rec late fee
drop_total_rec_late_fee(loan)

#Drop recoveries
drop_recoveries(loan)

#Drop collection recovery fee
drop_collection_recovery_fee(loan)

#Drop last payment date
drop_last_pymnt_d(loan)

#Drop last credit pull date
drop_last_credit_pull_d(loan)

#Drop Collections 12 months
drop_collections_12_mths_ex_med(loan)

#Drop Policy Code
drop_policy_code(loan)

#Drop Application Type
drop_application_type(loan)

#Drop acc_now_delinq
drop_acc_now_delinq(loan)

#Drop total colllection amount
drop_tot_coll_amt(loan)

#Drop Total Current Balance
drop_tot_cur_bal(loan)

#Fill na total rev hi lim
fill_na_total_rev_hi_lim(loan)

#Defining features and Categorical Features

features = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'term', 'int_rate',
            'installment', 'grade', 'sub_grade', 'emp_length', 'home_ownership',
            'annual_inc', 'verification_status', 'purpose', 'dti',
            'delinq_2yrs', 'inq_last_6mths', 'open_acc', 'revol_bal', 'revol_util',
            'total_acc', 'initial_list_status', 'total_pymnt', 'total_pymnt_inv',
            'total_rec_prncp', 'total_rec_int', 'last_pymnt_amnt',
            'total_rev_hi_lim', 'loan_status_coded']

categorical = ['term', 'grade', 'emp_length', 'home_ownership', 'verification_status',
               'purpose', 'initial_list_status']

loan = loan[features]

#One Hot Encoded
loan_one_hot_encoded = one_hot_encoder(loan)

# Train-Test split
y = loan_one_hot_encoded.loan_status_coded
X = loan_one_hot_encoded.drop("loan_status_coded", axis=1)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

print("Shape of x_train: ", x_train.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of x_test: ", x_test.shape)
print("Shape of y_test: ", y_test.shape)

# Neural Network model
y_train = encode_neural_net_y(y_train)
y_test = encode_neural_net_y(y_test)

# create model
model = Sequential()
model.add(Dense(35, input_dim=65, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(3, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

print(model.summary())

model.fit(np.array(x_train), np.array(y_train), epochs=30, batch_size=40, verbose=0)

scores = model.evaluate(np.array(x_test), np.array(y_test), verbose=0)
print("====================[TEST SCORE]====================")
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))












 




































