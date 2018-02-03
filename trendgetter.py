# -*- coding: utf-8 -*-
import google_trends_curl as gtc
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

countries = gtc.get_countries()

app.layout = html.Div(children=[
    html.H1(children='Welcome to Trendgetter'),

    html.Div(children='''
        Trendgetter: Get the news trends.
    '''),

    html.Div([
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in countries],
            value=''
        ),
    ], style={'width': '20%', 'display': 'inline-block'}),

    html.Div(id='output-google-trends')
])

@app.callback(
    dash.dependencies.Output('output-google-trends', 'children'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_google_trends(country):
    google_trends = gtc.get_google_trends(country)
    res = [html.H3(trend['keyword']) for trend in google_trends]
    return res

if __name__ == '__main__':
    app.run_server(debug=True)
