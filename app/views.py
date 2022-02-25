# from operator import index
# from email import message
from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns index page
    '''

    message = 'News on the go'
    return render_template('index.html',message = message)

@app. route('/news/<news_id>')
def news(news_id):
    '''
    View news page function
    '''

    return render_template('news.html,id = news_id')    