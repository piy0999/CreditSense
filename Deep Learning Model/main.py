# import modules
import pandas as pd
import numpy as np
from feature_eng import trim_features
from trim_data import drop_null_columns, categorize_target, split_loan_in_progress
from one_hot_encoding import one_hot_encoder
from one_hot_encoding import encode_neural_net_y
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
from oversample_by_SMOTE import oversample_smote
import matplotlib.pyplot as plt
import feature_index
import sys

# sys info
print(sys.version)

# load data
loan = pd.read_csv('loan.csv')

# pre-process data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)

# Feature Engineering by EDA
trim_features(loan)

# one-hot encoding
loan = loan[feature_index.features]
loan_one_hot_encoded = one_hot_encoder(loan)

# Train-Test split
y = loan_one_hot_encoded.loan_status_coded
X = loan_one_hot_encoded.drop("loan_status_coded", axis=1)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# oversample_SMOTE
x_train, y_train = oversample_smote(x_train, y_train)

# Neural Network model
y_train = encode_neural_net_y(y_train)
y_test = encode_neural_net_y(y_test)

model = Sequential()
model.add(Dense(34, input_dim=65, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
hist = model.fit(np.array(x_train), np.array(y_train), epochs=10, batch_size=50,
                 validation_data=(np.array(x_test), np.array(y_test)), verbose=2)
plt.plot(hist.history["acc"], label='acc')
plt.plot(hist.history["val_acc"], label='val_acc')
plt.legend()
plt.savefig('performance')
plt.show()

scores = model.evaluate(np.array(x_test), np.array(y_test), verbose=0)
print("====================[TEST SCORE]====================")
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# Save model
model.save('neural_net_model.h5')
