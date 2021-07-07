import math
import os

import pandas as pd
import yfinance as yf
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, model_from_json, load_model
from tensorflow.keras.layers import Dense, LSTM

from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

import matplotlib.pyplot as plt
import mplfinance as mpf
plt.style.use('fivethirtyeight')

TimeseriesGenerator()

def get_data(name):
    ''' Fetches the data from the YFinance API. Takes 1 argument name for the name of stock data to be fetched '''

    df = yf.download(name)
    data = df.filter(['Close'])

    return data


def get_dataset(name):
    ''' Fetches the data values (dataset) from the YFinance API. Takes 1 argument name for the name of stock data to be fetched '''

    df = yf.download(name)
    data = df.filter(['Close'])
    dataset = data.values

    return dataset


def scale_data(dataset):
    ''' Scales the dataset in the range (0, 1) '''

    scalar = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scalar.fit_transform(dataset)

    return scaled_data


def create_training_dataset(scaled_data, training_data_len):
    ''' Creates training dataset for training the LSTM model by cutting the complete dataset by training_data_set length '''

    # Create the training dataset
    # Creating the scaled training dataset
    train_data = scaled_data[0:training_data_len, :]
    # Split the data into x_train and y_train data sets
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])

    # Convert the x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    return x_train, y_train


def create_model(x_train):
    ''' Creates LSTM model with 4 layers \n 1 - LSTM  - 50 nuerons \n 2 - LSTM  - 50 nuerons \n 3 - Dense - 25 nuerons \n 3 - Dense -  1 nueron'''

    # Building the LTSM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True,
                   input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    return model


def train_model(model, x_train, y_train):
    ''' Compiles, trains and saves the inputed model '''

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error',
                  metrics=['accuracy'])

    # # Train the model
    if os.path.exists('./prediction.json'):
        # load json and create model
        json_file = open('./prediction.json', 'r')

        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)

        # load weights into new model
        model.load_weights("./prediction.h5")

        model.save('./prediction.hdf5')
        model = load_model('./prediction.hdf5')
    else:
        model.fit(x_train, y_train, epochs=100, batch_size=1)
        with open("./prediction.json", "w") as json_file:
            json_file.write(model.to_json())
        model.save_weights("./prediction.h5")

    # model.fit(x_train, y_train, epochs=1, batch_size=1)

    return model


def create_test_dataset(scaled_data, training_data_len, dataset):
    ''' Creates test dataset for predicting the LSTM model by cutting the complete dataset by training_data_set length '''

    # create testing dataset
    # Create new array containing scaled values from index 1543 to 2003
    test_data = scaled_data[training_data_len - 60:, :]

    # Create the datasets x_test and y_test
    x_test = []
    y_test = dataset[training_data_len:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])

    # Convert to numpy array
    x_test = np.array(x_test)

    # Reshape the data
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return x_test


def predict_stock(name):
    ''' Predicts the stock using LSTM type model '''

    ds = get_dataset(name)
    data = get_data(name)
    sd = scale_data(ds)

    for i in range(2):
        train_data_len = int(len(ds)*0.9)

        x_train, y_train = create_training_dataset(sd, train_data_len)

        model = create_model(x_train)
        train_model(model, x_train, y_train)

        x_test = create_test_dataset(sd, train_data_len, ds)

        # Get the models predicted price values

        scalar = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scalar.fit_transform(ds)

        predictions = model.predict(x_test)
        predictions = scalar.inverse_transform(predictions)

        ds.append(predictions)

    return predictions, data, train_data_len


def plot_data(predictions, data, training_data_len):
    ''' Plots the training data, test data ad predicted data '''
    # Plot the data
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    # Visualize the model
    plt.figure(figsize=(16, 8))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(train['Close'])
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')

    plt.show()


STOCK = "^BSESN"
prediction, data, train_data_length = predict_stock(STOCK)
plot_data(prediction, data, train_data_length)
