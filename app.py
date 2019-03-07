import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('mtcars.csv')

print(df)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i, 'value': i} for i in df.columns.values],
                value='aaa'
            ),
             dcc.Dropdown(
                id='yaxis',
                options=[{'label': i, 'value': i} for i in df.columns.values],
                value='aaa'
            )
        ],
        style={'width': '50%', 'display': 'inline-block'}),
    dcc.Graph(id='mgp-w')
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
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': xaxis},
                yaxis={'title': yaxis},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)