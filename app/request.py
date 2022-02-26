from app import app
import urllib.request,json
from .models import news

News = news.News

#getting api keys
api_key = app.config['NEWS_API_KEY']
api_url_everything = app.config['NEWS_API_EVERYTHING']
api_get_top_headlines_sources = app.config['NEWS_API_TOP_HEADLINES_SOURCES']

#getting the news base url
# base_url = app.config["NEWS_API_BASE_URL"]

#create get sources function that takes news category as argument
def get_sources():
    get_news_url = api_get_top_headlines_sources.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # news_results = []
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            
        
        return news_results_list


def get_news(query):
    '''
    Function that gets the json response to url request

    '''

    get_news_url = api_url_everything.format(query, api_key)


    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = []
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
        
        return news_results

#function that takes in a list of dictionaries
def process_results(news_list):
    '''
    Function that process the news result and transform to a list 
    
    Args:
        news_results: A list of dictionaries that contain news default_parser_list

    Returns:  
        news_results: A list of news objects 
    '''

    news_results = []
    for news_item in news_list:
        url = news_item.get('url')
        title = news_item.get('title')
        urlToImage = news_item.get('urlToImage')
        author = news_item.get('author')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        news = News(url, title, urlToImage, author, description, publishedAt, content)

        news_results.append(news)                

    return news_results           

