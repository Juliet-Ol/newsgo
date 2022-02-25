import unittest
from models import news
News = news.news

#creating test classes

class NewsTest(unittest.TestCase):
    '''
    Test Class to test behaviour of news class
    '''
    def setUp(self):
        '''
        Set up method to run before every Test
        '''
        self.new_news = News (1234, 'apples and more apples', 'for apples','https://newsapi.org/v2/everything?q=Apple&from=2022-02-25&sortBy=popularity&apiKey=API_KEY')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()        