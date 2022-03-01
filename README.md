# NEWS ON THE GO

## Application Link

https://julietol.herokuapp.com/

## Description

NEWS ON THE GO is a news app for anyone who is busy and has no time to sit down and catch up on the news or someone who wants an overview of what is happening around the world and even in their locality.

The app is designed with busy people in mind who are always on the move and also those who would like to skim through the news and know what is happening.

## API Reference

https://newsapi.org/

## Installations

Guide to install News on the go
 
### Clone this repository

 git clone https://github.com/Juliet-Ol/newsgo

 - [Get into the cloned directory]

 cd newsgo

 - [Create and activate your virtual environment:]

 mkvirtualenv virtual

 - [Install dependancies within your active environment]

 ### Environment variables:

 Create a file called .env in the root folder

 (virtual)$ touch .env

 - [Add the following lines to the file as seen in config.py file]

 NEWS_API_TOP_HEADLINES_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
NEWS_API_TOP_HEADLINES_SOURCE = 'https://newsapi.org/v2/top-headlines/sources={}?apiKey={}'
NEWS_API_EVERYTHING = 'https://newsapi.org/v2/everything?q={}&apiKey={}'

## Start the flask server

(Virtual)$ flask run

or

(Virtual)$ python3 run.py

**Features and BDD**

Users can access news sources about  what is going on in there country or around the world in different languages and news houses.

**Technology Used**

Framework: Flask language Python

### Developed with

Structure: Bootstrap, HTML 
Styles: CSS

### Author

Design and developed by: Juliet Oluoch


## License Copyright

Copyright (c) 2022 Juliet Oluoch

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.







