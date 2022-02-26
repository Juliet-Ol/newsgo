
from app import app
from flask import request
#from app.request import get_news

from app.request import get_news, get_sources
from flask import render_template



@app.route('/')
def home():
    sources = get_sources()
    return render_template('index.html', sources = sources)

@app.route('/source')
def index():
    sources = get_sources()
    headline = get_news(request.args.get('s'))
    return render_template('index.html', headline = headline, sources = sources)


@app.route('/search', methods=['POST'])
def search():
    search_value = request.form['search']
    headline = get_news(search_value)
    return render_template('index.html', headline = headline, search = search_value)

 

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
    
        