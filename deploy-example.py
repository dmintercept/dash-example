import dash

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

from dash.dependencies import Input, Output


import random

app = dash.Dash()
server = app.server
app.layout = html.Div(children=
                          [html.H4('Graph Example'),
                           dcc.Graph(id='main-graph',
                                     figure={'data':data}),
                           dcc.Interval(id='graph-update',
                                        interval=3 * 1000, 
                                        n_intervals=0)
                          ]
                     )
###call back to update the data displayed in the graph
@app.callback(dash.dependencies.Output('main-graph', 'figure'),
    [dash.dependencies.Input('graph-update', 'n_intervals')])
def update(n_intervals):
    trace = go.Scatter(
                x=[1, 2, 3, 4],
                y=random.sample(range(30),4)
    )
    data = [trace]
    return go.Figure(data=data)

if __name__ == '__main__':
    app.run_server(debug=False)