import math
import os
from pathlib import Path

import pandas as pd
import investpy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, model_from_json, load_model
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

import datetime

# get the path in which models are stored
file_path = str(Path(__file__).resolve().parent.parent) + '/static/machine_learning/prediction'

def get_data(name):
    """ Fetches the data from the Investing.com API\n 
        Takes the name as a parameter in format of 
        yfinance abbriviations """

    now = datetime.datetime.now().date()
    now = f'{now.day}/{now.month}/{now.year}'

    df = investpy.get_index_historical_data(
        index=name, from_date="01/01/1800", to_date=now, country="INDIA")
    dataset = df.filter(['Close'])
    return df, dataset


def scale_data(dataset):
    """ Scales the dataset in the range (0,1) suitable for the
        LSTM model.\n Takes dataset as an argument of the type dataframe"""

    scalar = MinMaxScaler(feature_range=(0, 1))
    train = scalar.fit_transform(dataset)
    return train, scalar


def create_prediction_list(train, n_input, model):
    """ Creates a prediction list which contains the value of 
        all the predictions made from the predict_data function """

    pred_list = []
    batch = train[-n_input:].reshape((1, n_input, 1))
    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:, 1:, :], [[pred_list[i]]], axis=1)
    return pred_list


def create_future_dates_list(df, n_input):
    """ Creates a list containing the future dates of the list in 1 day interval"""

    add_dates = [df.index[-1] +
                 pd.DateOffset(days=x) for x in range(0, n_input+1)]
    future_dates = pd.DataFrame(index=add_dates[1:], columns=df.columns)
    return future_dates


def proj_dataset(scalar, pred_list, future_dates, n_input, df):
    """ Creates a dataframe containing both the previous and the final data"""

    df_predict = pd.DataFrame(scalar.inverse_transform(
        pred_list), index=future_dates[-n_input:].index, columns=['Prediction'])
    df_proj = pd.concat([df['Close'], df_predict], axis=1)
    return df_proj


def predict_data(epoch, n_input, train, name):
    """ Makes actual predictions of the data inputted """

    # creating a time series generator
    generator = TimeseriesGenerator(
        train, train, length=n_input, batch_size=10, sampling_rate=1, stride=1)

    # creating the LSTM model
    model = Sequential()
    model.add(LSTM(200, activation='relu', input_shape=(n_input, 1)))
    model.add(Dropout(0.15))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

    # Train the model
    if os.path.exists(file_path + f'/{name}/prediction.json'):
        # load json and create model
        json_file = open(
            file_path + f'/{name}/prediction.json', 'r')

        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)

        # load weights into new model
        model.load_weights(
            file_path + f'/{name}/prediction.h5')

        model.save(
            file_path + f'/{name}/prediction.hdf5')
        model = load_model(
            file_path + f'/{name}/prediction.hdf5')
    else:
        model.fit(generator, epochs=epoch, verbose=1)
        with open(file_path + f'/{name}/prediction.json', "w") as json_file:
            json_file.write(model.to_json())
        model.save_weights(
            file_path + f'/{name}/prediction.h5')
    # model.fit(generator, epochs=epoch, verbose=1)
    return model


def timeseries_prediction(days, index):

    df, dataset = get_data(index)
    train, scalar = scale_data(dataset)
    future_dates = create_future_dates_list(df, days)

    model = predict_data(100, days, train, index)

    pred_list = create_prediction_list(train, days, model)

    df_proj = proj_dataset(scalar, pred_list, future_dates, days, df)
    print(df_proj)


timeseries_prediction(365, "nifty 50")
