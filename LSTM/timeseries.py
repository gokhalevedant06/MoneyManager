import math
import os
import pandas as pd
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, model_from_json, load_model
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
import matplotlib.pyplot as plt


def get_data(name):
    """ Fetches the data from the yahoo finance API\n 
        Takes the name as a parameter in format of 
        yfinance abbriviations """

    df = yf.download(name)
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


def predict_data(epoch, n_input, train):
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
        model.fit(generator, epochs=epoch, verbose=1)
        with open("./prediction.json", "w") as json_file:
            json_file.write(model.to_json())
        model.save_weights("./prediction.h5")
    # model.fit(generator, epochs=epoch, verbose=1)
    return model


def plot_data(df, df_proj):
    """ Plots the data in matplotlib """
    plt.figure(figsize=(16, 8))
    plt.title("Close Price History")
    plt.plot(df['Close'])
    plt.plot(df_proj[['Prediction']])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.legend(['Close', 'Prediction'])
    plt.show()


def main():
    days = 365

    df, dataset = get_data("^BSESN")
    train, scalar = scale_data(dataset)
    future_dates = create_future_dates_list(df, days)

    model = predict_data(100, days, train)

    pred_list = create_prediction_list(train, days, model)

    df_proj = proj_dataset(scalar, pred_list, future_dates, days, df)

    plot_data(df, df_proj)


if __name__ == '__main__':
    main()
