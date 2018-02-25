import feature_index
import pandas as pd
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder


def encode_neural_net_y(y):
    encoder = LabelEncoder()
    encoder.fit(y)
    encoded_y = encoder.transform(y)
    new_y = np_utils.to_categorical(encoded_y)
    return new_y


def one_hot_encoder(loan):
    print("====================[Data Types]====================")
    print(loan.dtypes)
    categorical_variables = feature_index.categorical
    loan_one_hot_encoded = pd.get_dummies(loan, columns=categorical_variables)
    return loan_one_hot_encoded
