from scraping import get_articles, foo
from peewee import * 

db = SqliteDatabase("fn-detect.db")

class Article(Model):
    class Meta:
        database = db

    url = TextField(unique=True)
    keywords = TextField(unique=False)
    publish_date = DateTimeField(null=True)
    text = TextField()
    title = TextField()
    summary = TextField()


db.connect()
db.create_tables([Article])

def crawl_articles(url):
    for i in get_articles(url):
        Article.create(
            url=i["url"],
            keywords=i["keywords"],
            publish_date=i["publish_date"],
            text=i["text"],
            title=i["title"],
            summary=i["summary"],
        )

crawl_articles("https://nytimes.com")
