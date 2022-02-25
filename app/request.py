# from email.mime import base
# from webbrowser import get
# from turtle import title
# from xml.sax import default_parser_list
from app import app
import urllib.request,json
from .models import news

News = news.News

#getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

def process_results(news_list):
    '''
    Function that process the news result and transform to a list 
    
    Args:
        news_list: A list of dictionaries that contain news default_parser_list

    Returns:  
        news_results: A list of news objects 
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('headline_title')
        story = story_item.get('story')
        author = author_item.get('author')

        if author:
            news_object = News(id,title,)
            news_results.append(news.object)                

    return news_results           

