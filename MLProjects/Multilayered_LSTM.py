#!/usr/bin/env python
# coding: utf-8
# This solution is not fully optimized
# importing all the appropriate libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential # Time Series requires a Sequential application
from keras.layers import LSTM, Dense, Dropout # Will be using densely connected layers
from sklearn.preprocessing import MinMaxScaler # Applying the scaler to our columns

# reading our dataset (the dataset is not available at this time) you'll have to insert your own
dataset_train = pd.read_csv('EUR_USD_TestSet1.csv')

# Using the first column of the dataset and converting them into a numpy array
# to be used as our training set
training_set = dataset_train.iloc[:, 1:2].values

# Applying a scaler with the feature range of 0 to 1
sc = MinMaxScaler(feature_range=(0, 1))

# Fitting the scaler on our training set
training_set_scaled = sc.fit_transform(training_set)

# Empty lists which will hold our x_train and y_train values
X_train = []
y_train = []

# Defining an appropriate range for the number of datasets we're training for
# and applying the scaled training set to x_train/y_train respectively
for i in range(12, 174):
    X_train.append(training_set_scaled[i - 12:i, 0])
    y_train.append(training_set_scaled[i, 0])
    
# Converting the x_train/y_train values to numpy arrays
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping the numpy array to the dataset we actually want to train for
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Calling the Sequential function
regressor = Sequential()

# Applying the regressor model with LSTM cell and a general dropout rate of 0.2
# which is ~20% of all the trained datasets over time
regressor.add(LSTM(units=40, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=40, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=40, return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=40))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1))
regressor.compile(optimizer='rmsprop', loss='mean_squared_error') # optimizing for rmsprop and loss will be MSE
regressor.fit(X_train, y_train, epochs=100, batch_size=4) # Using the x_train/y_train values to fit over 100 epochs with a batch size of 4 values passed into the learner function

# Defining the test set which we will measure our trained dataset against
dataset_test = pd.read_csv('EUR_USD_TestSet1_Copy.csv')
real_price = dataset_test.iloc[:, 1:2].values

# Concatenating the 2 values in respective order and applying reshapes to turn
# the numpy scaler back into data points on the matplotlib
dataset_total = pd.concat((dataset_train['o'], dataset_test['o']), axis=0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 12:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)

# sampling of the x_test dataset
X_test = []
for i in range(12, 45):
    X_test.append(inputs[i-12:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Using the prediction model to predict prices against x_test dataset
predicted_price = regressor.predict(X_test)
predicted_price = sc.inverse_transform(predicted_price)

# Plotting the result
plt.plot(real_price, color='red', label='Real EUR/USD Price')
plt.plot(predicted_price, color='blue', label='Predicted EUR/USD Price')
plt.title('EUR/USD Price Predictions')
plt.xlabel('Time')
plt.ylabel('EUR/USD Price')
plt.legend()
plt.show()




