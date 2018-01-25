import News
from newsapi import NewsApiClient
from textblob import TextBlob

newsapi = NewsApiClient(api_key='2de8bebd4cc24d51bc4bf38508bbcd7d')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          language='en'
                                          )
news = {}

def main():
    news = News.News()
    news.grab_article_title_descrip(**top_headlines)
    news = news.newsArticles


if __name__ == "__main__":
    main()
