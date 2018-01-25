
#print("Description: %s" % top_headlines['articles'][0]['description'])
#print("Title: %s" % top_headlines['articles'][0]['title'])
class News:
    newsArticles = {}

    def grab_article_title_descrip(self,**articles):
        for x in range(len(articles)):
            articleTitle = articles['articles'][x]["title"]
            url = articles['articles'][x]["url"]
            article = {"articleTitle" : articleTitle, "url": url}
            self.newsArticles[x] = article
