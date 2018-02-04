# -*- coding: utf-8 -*-
import itertools
import google_trends_curl as gtc
import tweets
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

countries = gtc.get_countries()

app.layout = html.Div(children=[
    html.H1(children='Welcome to Trendgetter'),

    html.Div(children='''
        Get the news trends
    '''),

    html.Div([
        html.Label('Password for Twitter trends:'),
        dcc.Input(id='tweet-pwd', type='text', placeholder='type password'),
    ]),

    html.Div([
        html.Label('Select a country '),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in countries],
            value=''
        ),
    ], style={'width': '20%', 'display': 'inline-block'}),

    html.Div(children=[
        html.Div(id='output-google-trends', style={'float': 'left', 'width': '45%'}),
        html.Div(id='output-twitter-trends', style={'float': 'left', 'width': '45%'})
    ], style={'clear': 'both'})

])

@app.callback(
    dash.dependencies.Output('output-google-trends', 'children'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_google_trends(country):
    google_trends = gtc.get_google_trends(country)
    res = [[html.H2('From Google Trends')]] + [[html.Div(children=trend['keyword'], style={'font-weight': 'bold'}), html.A(trend['title'], \
        href=trend['url']), html.Br(), html.Label('source: {}, date: {}'.format(trend['source'], trend['publication_date'])), html.Br(), html.Br()] for trend in google_trends]
    res = list(itertools.chain(*res))
    return res

@app.callback(
    dash.dependencies.Output('output-twitter-trends', 'children'),
    [dash.dependencies.Input('country-dropdown', 'value'),
     dash.dependencies.Input('tweet-pwd', 'value')]
)
def update_twitter_trends(country, password):
    twitter_trends = tweets.get_trends(country, password)
    # res = [html.H2('From Twitter')] + [html.H3(trend['keyword']) for trend in twitter_trends]
    res = [[html.H2('From Twitter')]] + [[html.A(trend['keyword'], href=trend['url']), html.Br(), html.Br()] for trend in twitter_trends]
    res = list(itertools.chain(*res))
    return res

if __name__ == '__main__':
    app.run_server(debug=True)
