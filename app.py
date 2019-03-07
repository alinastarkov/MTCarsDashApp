import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('mtcars.csv')
print(df['gear'].value_counts()
)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': 'white'}, children=[
    html.H1(children="All you need to know about Motor Trend Cars", style={
            'font-weight': 'bold',
            'font-family': 'helvetica',
            'textAlign': 'center',
            'color': '#1B1B1C'
        }),
      html.H2(children="Please choose the x-axis and the y-axis category", style={
            'font-family': 'helvetica',
            'textAlign': 'center',
            'color': '#1B1B1C'
        }),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i, 'value': i} for i in df.columns.values],
                value='mpg'
            )
        ],
        style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center', 'margin': '0 0 0 19%'}),
    html.Div([
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i, 'value': i} for i in df.columns.values],
                value='model'
            )
        ], style={'width': '30%', 'float': 'right', 'display': 'inline-block', 'margin': '0 20% 0 0'})
    ]),
    dcc.Graph(id='mgp-w'),
    
])

@app.callback(
    dash.dependencies.Output('mgp-w', 'figure'),
    [dash.dependencies.Input('xaxis', 'value'),
     dash.dependencies.Input('yaxis', 'value')])
def update_graph(xaxis, yaxis):

    return {
        'data': [go.Scatter(
            x=df[xaxis],
            y=df[yaxis],
            text=df['model'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.8, 'color': 'white'}
            }
        )],
            'layout': go.Layout(
                height=450,
                xaxis={'type': 'log', 'title': xaxis},
                yaxis={'title': yaxis},
                margin={'l': 160, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest')
    }


if __name__ == '__main__':
    app.run_server(debug=True)