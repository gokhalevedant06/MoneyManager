from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import investpy

import plotly.express as px
import plotly.graph_objs as go
import datetime

# preparing the dataframe


def prepare_dataframe(df):
    ''' Prepares Dataframe for the plotly graph plotting '''

    df = df.drop(columns=['Volume', 'Currency'])
    date = df.index.strftime("%b %d %Y")
    date = date.to_flat_index()
    df.reset_index(inplace=True, drop=True)
    df.set_index(date, inplace=True, drop=True)

    return df


now = datetime.datetime.now().date()

now = f"{now.day}/{now.month}/{now.year}"

df_nifty = investpy.get_index_historical_data(
    index="Nifty 50", from_date='01/01/1995', to_date=now, country="india", interval="Daily")

df_sensex = investpy.get_index_historical_data(
    index="bse sensex", country="INDIA", from_date="01/01/2000", to_date=now, interval="Daily")

df_nifty_prep = prepare_dataframe(df_nifty)
df_sensex_prep = prepare_dataframe(df_sensex)


# Dash app code

app = DjangoDash('sensex_nifty_graph', external_stylesheets=[
                 dbc.themes.BOOTSTRAP])

# stup the layout

ohlc_options = [{"label": "All", "value": "all"}]
ohlc_options += [{'label': i, 'value': i} for i in df_nifty_prep.columns]

timeseries_options = [
    {"label": "This Week", 'value': 7},
    {"label": "This Month", 'value': 30},
    {"label": "This Year", 'value': 365},
    {"label": "Ten Years", 'value': 3650},
    {"label": "Max", 'value': 10000},
]

nifty_card = dbc.CardBody([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='ohlc_dropdown_nifty',
                options=ohlc_options,
                value="Open"
            )
        ]),
        dbc.Col([
            dcc.Dropdown(
                id="timeseries_selector_nifty",
                options=timeseries_options,
                value=10000
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

sensex_card = dbc.CardBody([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='ohlc_dropdown_sensex',
                options=ohlc_options,
                value="Open"
            )
        ]),
        dbc.Col([
            dcc.Dropdown(
                id="timeseries_selector_sensex",
                options=timeseries_options,
                value=10000
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

tabs = dbc.Tabs([
    dbc.Tab(sensex_card, label="Sensex"),
    dbc.Tab(nifty_card, label="Nifty")
])

app.layout = html.Div([
    dbc.Card([
        dbc.CardHeader(children="Sensex and Nifty Graphs"),
        dbc.CardBody(tabs)
    ])
])


@app.callback(
    Output('nifty_graph', 'figure'),
    Output('sensex_graph', 'figure'),
    Input('ohlc_dropdown_nifty', 'value'),
    Input('ohlc_dropdown_sensex', 'value'),
    Input('timeseries_selector_nifty', 'value'),
    Input('timeseries_selector_sensex', 'value'),
)
def update_graph(selected_ohlc_nifty, selected_ohlc_sensex, timeseries_selector_nifty, timeseries_selector_sensex):

    end = datetime.datetime.now().date()

    nifty_start = str(end - datetime.timedelta(days=timeseries_selector_nifty))
    sensex_start = str(
        end - datetime.timedelta(days=timeseries_selector_sensex))

    end = str(end)

    nifty_data = df_nifty_prep[(df_nifty.index > str(nifty_start)) & (
        df_nifty.index < str(end))]

    sensex_data = df_sensex_prep[(df_sensex.index > str(sensex_start)) & (
        df_sensex.index < str(end))]

    colors = {'Open': '#4e73df', 'High': '#1cc88a',
                  'Low': '#e74a3b', 'Close': '#36b9cc'}

    if selected_ohlc_nifty == 'all':
        nifty = go.Figure(
            go.Candlestick(
                x=nifty_data.index,
                open=nifty_data['Open'],
                high=nifty_data['High'],
                low=nifty_data['Low'],
                close=nifty_data['Close'],
                increasing_line_color='green',
                decreasing_line_color='red'
            )
        )
        nifty.update_layout(xaxis_rangeslider_visible=False)
        
        sensex = px.line(
            sensex_data['Open'],
            title=f'Sensex 50 : {selected_ohlc_sensex}',
            height=500,
        )

    elif selected_ohlc_sensex == 'all':
        sensex = go.Figure(
            go.Candlestick(
                x=sensex_data.index,
                open=sensex_data['Open'],
                high=sensex_data['High'],
                low=sensex_data['Low'],
                close=sensex_data['Close'],
                increasing_line_color='green',
                decreasing_line_color='red'
            )
        )
        sensex.update_layout(xaxis_rangeslider_visible=False)

        nifty = px.line(
            nifty_data['Open'],
            title=f'Nifty 50 : {selected_ohlc_nifty}',
            height=500,
        )
    else:
        
        color_seq_nifty = []
        color_seq_sensex = []
        color_seq_nifty.append(colors[selected_ohlc_nifty])
        color_seq_sensex.append(colors[selected_ohlc_sensex])

        nifty_data = nifty_data[selected_ohlc_sensex]
        sensex_data = sensex_data[selected_ohlc_sensex]

        nifty = px.line(
            nifty_data,
            title=f'Nifty 50 : {selected_ohlc_nifty}',
            height=500,
            color_discrete_sequence=color_seq_nifty
        )

        sensex = px.line(
            sensex_data,
            title=f'Sensex 50 : {selected_ohlc_sensex}',
            height=500,
            color_discrete_sequence=color_seq_sensex
        )

    return nifty, sensex
