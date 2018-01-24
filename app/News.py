
#print("Description: %s" % top_headlines['articles'][0]['description'])
#print("Title: %s" % top_headlines['articles'][0]['title'])
class News:

    def grab_article_title_descrip(self,**articles):
        for x in range(len(articles)):
            articleTitle = articles['articles'][x]["title"]
            description = articles['articles'][x]["description"]
            print("Title: %s" % articleTitle)
            print("Description: %s\n" % articleTitle)
