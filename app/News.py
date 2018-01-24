from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='2de8bebd4cc24d51bc4bf38508bbcd7d')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          language='en'
                                          )
#print("Description: %s" % top_headlines['articles'][0]['description'])
#print("Title: %s" % top_headlines['articles'][0]['title'])


def grab_article_title_descrip(**articles):
    for x in range(len(articles)):
        articleTitle = articles['articles'][x]["title"]
        description = articles['articles'][x]["description"]
        print("Title: %s" % articleTitle)
        print("Description: %s\n" % articleTitle)

grab_article_title_descrip(**top_headlines)
