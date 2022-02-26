class News:
    '''
    News class to define news objects
    '''

    def __init__(self, url, title, author, description, publishedAt,content, urlToImage):
        self.url = url
        self.title =title
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = urlToImage