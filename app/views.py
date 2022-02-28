
from crypt import methods
from app import app
from flask import request
from app.request import get_news

from app.request import get_sources
from flask import render_template,request,redirect,url_for



@app.route('/', methods=['POST', 'GET'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()

    if request.method == 'POST':
        search_value = request.form['search']
        news_list = get_news(search_value)
    else:
        news_list = get_news(request.args.get('s'))

    return render_template('index.html', news_list = news_list, sources = sources)


# @app.route('/search', methods=['POST'])
# def search():
#     '''
#     View root page function that returns search page and its data
#     '''
     
#     search_value = request.form['search']
#     headline = get_news(search_value)
#     return render_template('index.html', headline = headline, search = search_value)

  
    
        