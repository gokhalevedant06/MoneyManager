from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objs as go
import datetime

import requests
from MoneyManager.settings import PREDICTION_URL
import pandas as pd

import investpy


def get_prediction_response(data, bse=True):
    '''
        Makes an http request to the server at https://money-manager-vit-pune-api/prediction/ and gets the prediction response\n
        Arguments:\n
        data: takes the name of ohlc i.e Open, High, Low or Close\n
        bse: if ser to true function will return bse data else will return nifty data
    '''

    if bse:
        try:
            return requests.post(url=PREDICTION_URL, json={"nifty_or_bse": "bse sensex", "ohlc": data})
        except ConnectionError:
            return "Error connecting to the server"
    else:
        try:
            return requests.post(url=PREDICTION_URL, json={"nifty_or_bse": "nifty 50", "ohlc": data})
        except ConnectionError:
            return "Error connecting to the server"


def prep_dataframe_pred(response, data):
    ''' 
        Prepares the dataframe to be plotted directly using plotly\n
        Arguments:\n
        response: takes the http response from server\n
        data: takes the name of ohlc i.e Open, High, Low or Close passed in the response
    '''
    df = pd.read_json(response.text)
    df.reset_index(inplace=True, drop=True)
    df.set_index(df['Date'], inplace=True, drop=True)
    df.drop(columns=['Date'], axis=1, inplace=True)

    df_pred = pd.concat([df[data], df['Prediction']],
                        axis=1, keys=[data, 'Prediction'])

    return df_pred


def get_sensex_nifty_data(sensex=True):
    now = datetime.datetime.now().date()
    diff = now - datetime.timedelta(days=2)

    now = f"{now.day}/{now.month}/{now.year}"
    diff = f"{diff.day}/{diff.month}/{diff.year}"
    if sensex:
        return investpy.get_index_historical_data(
            index="bse sensex", country="INDIA", from_date=diff, to_date=now, interval="Daily")
    else:
        return investpy.get_index_historical_data(
            index="nifty 50", country="INDIA", from_date=diff, to_date=now, interval="Daily")


df_sensex = get_sensex_nifty_data()

df_nifty = get_sensex_nifty_data(sensex=False)

app = DjangoDash('sensex_nifty_prediction_graph', external_stylesheets=[
                 dbc.themes.BOOTSTRAP])

ohlc_options = [
    {
        "label": "Open",
        "value": "Open"
    },
    {
        "label": "High",
        "value": "High"
    },
    {
        "label": "Low",
        "value": "Low"
    },
    {
        "label": "Close",
        "value": "Close"
    },
]

sensex_card = dbc.CardBody([
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="Open", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_sensex.tail(1)['Open'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-primary shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="High", className="text-xs font-weight-bold text-success text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_sensex.tail(1)['High'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-success shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="low", className="text-xs font-weight-bold text-danger text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_sensex.tail(1)['Low'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-danger shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="close", className="text-xs font-weight-bold text-info text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_sensex.tail(1)['Close'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-info shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='ohlc_dropdown_sensex',
                options=ohlc_options,
                value="Open"
            )
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Loading([
                dcc.Graph(id="sensex_graph")],
                type="dots",
                fullscreen=False,
                color="#119DFF"
            )
        ])
    ])
])

nifty_card = dbc.CardBody([
    dbc.Row([
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="Open", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_nifty.tail(1)['Open'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-primary shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="High", className="text-xs font-weight-bold text-success text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_nifty.tail(1)['High'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-success shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="low", className="text-xs font-weight-bold text-danger text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_nifty.tail(1)['Low'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-danger shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            children="close", className="text-xs font-weight-bold text-info text-uppercase mb-1"),
                        dbc.CardBody(
                            children=f"{df_nifty.tail(1)['Close'].values[0]}", className="h5 mb-0 font-weight-bold text-gray")
                    ],
                    className="border-left-info shadow h-100 py-2"
                ),
            ],
            className="col-xl-3 col-md-6 mb-4"
        ),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='ohlc_dropdown_nifty',
                options=ohlc_options,
                value="Open"
            )
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Loading([
                dcc.Graph(id="nifty_graph")],
                type="dots",
                fullscreen=False,
                color="#119DFF"
            )
        ]),
    ])
])

tabs = dbc.Tabs([
    dbc.Tab(sensex_card, label="Sensex"),
    dbc.Tab(nifty_card, label="Nifty"),
])


app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            tabs
        ])
    ])
], className="p-5")


@app.callback(
    Output('nifty_graph', 'figure'),
    Output('sensex_graph', 'figure'),
    Input('ohlc_dropdown_nifty', 'value'),
    Input('ohlc_dropdown_sensex', 'value'),
)
def update_graph(selected_ohlc_nifty, selected_ohlc_sensex):

    colors = {'Open': '#4e73df', 'High': '#1cc88a',
              'Low': '#e74a3b', 'Close': '#36b9cc'}

    colors_pred = {'Open': '#FF1600', 'High': '#00DFFF',
                   'Low': '#00FFA3', 'Close': '#0041FF'}

    color_seq_sensex_pred = []
    color_seq_nifty_pred = []

    color_seq_sensex_pred.append(
        colors[selected_ohlc_sensex])
    color_seq_sensex_pred.append(
        colors_pred[selected_ohlc_sensex])

    color_seq_nifty_pred.append(
        colors[selected_ohlc_nifty])
    color_seq_nifty_pred.append(
        colors_pred[selected_ohlc_nifty])

    prediction_sensex_response = get_prediction_response(
        selected_ohlc_sensex, bse=True)

    sensex_pred_data = prep_dataframe_pred(
        prediction_sensex_response, selected_ohlc_sensex)

    sensex = px.line(
        sensex_pred_data,
        title=f'Sensex 50 (Prediction) : {selected_ohlc_sensex}',
        height=500,
        color_discrete_sequence=color_seq_sensex_pred
    )

    prediction_nifty_response = get_prediction_response(
        selected_ohlc_nifty, bse=False)

    nifty_pred_data = prep_dataframe_pred(
        prediction_nifty_response, selected_ohlc_nifty)

    nifty = px.line(
        nifty_pred_data,
        title=f'Nifty 50 (Prediction) : {selected_ohlc_nifty}',
        height=500,
        color_discrete_sequence=color_seq_nifty_pred
    )

    return nifty, sensex
