import csv
import os
import requests

from random import randint 
from numpy import array
from numpy import argmax
from pandas import DataFrame
from pandas import concat
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import TimeDistributed
from keras.layers import RepeatVector
import numpy as np
import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.columns = ['HKID', 'Date','Event']
train = train.sort_values('HKID')
train = train.sort_values('Date')

# unique_valu = train.Event.unique()
uniq_lab,idx = np.unique(train['Event'],return_inverse=True)
zipped = zip(uniq_lab,idx)
train['Event'] = idx

train = train.groupby('HKID')['Event'].apply(list)

#preview the data to be trained
train.head()

def get_sequence(HKID):
    row = train[HKID][-203:]
    if len(row)<20:
        row = row + row
    return row
# one hot encode sequence
def one_hot_encode(sequence, n_unique=6475):
    encoding = list()
    for value in sequence:
        vector = [0 for _ in range(n_unique)]
        vector[value] = 1
        encoding.append(vector)
    return array(encoding)

# decode a one hot encoded string
def one_hot_decode(encoded_seq):
    return [argmax(vector) for vector in encoded_seq]

# convert encoded sequence to supervised learning
def to_supervised(sequence, n_in, n_out):
    # create lag copies of the sequence
    df = DataFrame(sequence)
    df = concat([df.shift(n_in-i-1) for i in range(n_in)], axis=1)
    # drop rows with missing values
    df.dropna(inplace=True)
    # specify columns for input and output pairs
    values = df.values
    width = sequence.shape[1]
    X = values.reshape(len(values), n_in, width)
    y = values[:, 0:(n_out*width)].reshape(len(values), n_out, width)
    return X, y

# prepare data for the LSTM
def get_data(HKID,n_in, n_out):
    # get the sequence
    sequence = get_sequence(HKID)
    # one hot encode
    encoded = one_hot_encode(sequence)
    # convert to X,y pairs
    X,y = to_supervised(encoded, n_in, n_out)
    return X,y


n_in = 20
n_out = 10
# a,b = get_data(n_in, n_out)
encoded_length = 6475
final_output = []
header = ['HKID','Event1','Event2','Event3','Event4','Event5','Event6','Event7','Event8','Event9','Event10']
final_output.append(header)

lene = 1

for index, row in train.iteritems():
    HKID = index
    # define LSTM
    # generate new random sequence
    X,y = get_data(HKID,n_in, n_out)
    lene = X.shape[0]
    c = lene/2
    e = c+1
    d = range(e,-1,-1)[:-1]
    for i in d:
        if(c%i == 0):
            break
    batch_size = i
    if(lene%batch_size !=0):
        batch_size = 1
    print ("Batch Size: ",batch_size)


    model = Sequential() #Depreciated in Keras 1.1.0
    model.add(LSTM(250, batch_input_shape=(batch_size, n_in, encoded_length), stateful=True))
    model.add(RepeatVector(n_out))
    model.add(LSTM(250, return_sequences=True, stateful=True))
    model.add(TimeDistributed(Dense(encoded_length, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
    
    # fit model for one epoch on this sequence
    earlyStopping = EarlyStopping(monitor='acc', min_delta=0, patience=10, verbose=0,mode='auto')
    model.fit(X, y, epochs=10, batch_size=batch_size, verbose=2, shuffle=False, callbacks=[earlyStopping])
    model.reset_states()
    
    yhat = model.predict(X, batch_size=batch_size, verbose=0)
    yhat_deco = one_hot_decode(yhat[lene-1])
    print ("yhat deco: ",yhat_deco)
    
    output = []
    output.append(HKID)
    for i in range(len(yhat_deco)):
        output.append(zipped[yhat_deco[i]][0])
    final_output.append(output)

with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(final_output)