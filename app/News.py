from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='2de8bebd4cc24d51bc4bf38508bbcd7d')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          language='en'
                                          )
print(top_headlines)
