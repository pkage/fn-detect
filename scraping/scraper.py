import newspaper

# takes an article URL, and inserts it after processing
def get_article(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    article.nlp()

    return _convert_article(article)


# Takes a newspaper url, and inserts each article
def get_articles(url):
    print("making paper")
    n = newspaper.build(url, memoize_articles=False)
    print("size", n.size())

    for article in n.articles:

        article.download()
        article.parse()
        article.nlp()

        yield _convert_article(article)

def _convert_article(a):
    return {
        'url': a.url,
        'keywords': a.keywords,
        'publish_date': a.publish_date,
        'text': a.text,
        'title': a.title,
        'summary': a.summary,
    }

    url = TextField(unique=True)
    keywords = TextField(unique=True)
    publish_date = DateTimeField()
    text = TextField()
    title = TextField()
    summary = TextField()

def foo():
    print("BAR")
