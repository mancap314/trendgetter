from flask import render_template
from app import app
import google_trends_curl as gtc

@app.route('/')
@app.route('/index')
def index():
    google_trends = gtc.get_google_trends('SWITZERLAND')
    return render_template('index.html', google_trends=google_trends)