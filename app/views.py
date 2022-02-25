# from operator import index
# from email import message
# from turtle import title
# from turtle import title
from flask import render_template
from app import app
#from app.request import get_news

@app.route('/')
def index():
    '''
    View root page function that returns index page
    '''

    message = 'News on the go'
    return render_template('index.html',message = message)

# @app. route('/news/<int:news_id>')
# def news(news_id):
#     '''
#     View news page function
#     '''

#     return render_template('news.html',id = news_id) 

# @app. route('/news/<int:news_story>')
# def news(news_story):
#     '''
#     View news page function
#     '''

#     return render_template('news.html',story = news_story)     

# def headline():
#     '''
#     View root page function that returns the index page and it's data
#     '''

#     title = 'Home - Keep up with the latest and hotest news'
#     return render_template('index.html', title = title) 

# @app.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     ''' 

#     # Getting news making headline
#     making_headline = get_news('headline')

#     return render_template('index.html', headline= making_headline)     
    
        