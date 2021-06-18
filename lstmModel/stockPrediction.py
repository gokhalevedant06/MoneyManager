import math
import pandas as pd
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM


def getData(company_name, oc):
    df = yf.download("JEPI")
    data = df.filter([type])
    dataset = data.values
    print(data)
    return dataset


getData("AAPL")
