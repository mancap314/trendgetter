# -*- coding: utf-8 -*-
import itertools
import google_trends_curl as gtc
import tweets
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.title = 'Trendgetter'
server = app.server

countries = gtc.get_countries()

# define the layout
app.layout = html.Div(children=[
    html.H1(children='Welcome to Trendgetter'),
    html.H2(children='Get the news trends', style={'font-weight': 'italic'}),
    html.Hr(style={'border-width': '1px', 'margin-top': '1em','margin-bottom': '1em'}),

    html.Div([
        html.Label('Password for Twitter trends:'),
        dcc.Input(id='tweet-pwd', type='text', placeholder='type password'),
    ]),

    html.Hr(style={'border-width': '1px', 'margin-top': '1em','margin-bottom': '1em'}),

    html.Div([
        html.Label('Select a country   '),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in countries],
            value=''
        ),
    ], style={'width': '20%', 'display': 'inline-block'}),

    html.Div(children=[
        html.Div(id='output-google-trends', style={'float': 'left', 'width': '50%'}),
        html.Div(id='output-twitter-trends', style={'float': 'left', 'width': '50%'})
    ], style={'clear': 'both'}),

    html.Hr(style={'border-width': '1px', 'margin-top': '1em','margin-bottom': '1em'}),
    html.Div(children=[
        html.Label('Author: '),
        html.A('Manuel Capel', href='https://mancap314.github.io/'),
        html.Label(', manuel.capel82[at]gmail.com, '),
        html.A('Github Repo', href='https://github.com/mancap314/trendgetter')
    ], style={'font-size': '0.8em'})
])

# call, format and show the Google Trends results if there is a change in the selected country
@app.callback(
    dash.dependencies.Output('output-google-trends', 'children'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_google_trends(country):
    if country is '': #return nothing if no country has been selected
        return ''
    google_trends = gtc.get_google_trends(country)
    #format the response
    res = [[html.H2('From Google Trends')]] + [[html.Div(children=trend['keyword'], style={'font-weight': 'bold'}), html.A(trend['title'], \
        href=trend['url']), html.Br(), html.Label('source: {}, date: {}'.format(trend['source'], trend['publication_date'])), html.Br(), html.Br()] for trend in google_trends]
    res = list(itertools.chain(*res))
    return res

# call, format and show the GoogleTweeter trends results if there is a change in the selected country and if the provided password is correct
@app.callback(
    dash.dependencies.Output('output-twitter-trends', 'children'),
    [dash.dependencies.Input('country-dropdown', 'value'),
     dash.dependencies.Input('tweet-pwd', 'value')]
)
def update_twitter_trends(country, password):
    if country is '': #return nothing if no country has been selected
        return ''
    twitter_trends = tweets.get_trends(country, password)
    # format the response
    res = [[html.H2('From Twitter')]] + [[html.A(trend['keyword'], href=trend['url']), html.Br(), html.Br()] for trend in twitter_trends]
    res = list(itertools.chain(*res))
    return res

if __name__ == '__main__':
    app.run_server(debug=True)
