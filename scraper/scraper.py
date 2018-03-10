import newspaper
import json

class Article:
    def __init__(self, url=None, authors=None, keywords=None, publish_date=None, text=None, title=None, summary=None):

        self.url = url
        self.authors = authors
        self.keywords = keywords
        self.publish_date = publish_date
        self.text = text
        self.title = title
        self.summary = summary
    
    def toJSON(self):
        return json.dumps(self.__dict__)

# takes an article URL, and returns it after processing
def get_article(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    article.nlp()

    return _convert_article(article)


# Takes a newspaper url, and yields each article
def get_articles(url):
    n = newspaper.build(url, memoize_articles=False)
    print(n.size())

    for article in n.articles:

        article.download()
        article.parse()
        article.nlp()

        yield _convert_article(article)

def _convert_article(a):
    return Article(url=a.url,
                   authors=a.authors,
                   keywords=a.keywords,
                   publish_date=a.publish_date,
                   text=a.text,
                   title=a.title,
                   summary=a.summary)


for i in get_articles("https://www.theguardian.com/uk"):
    print(i.title, i.keywords)
