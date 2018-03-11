from flask import Flask, g
import sqlite3
from .data import twitter
import botometer
import json

DATABASE = '../scraper/fn-detect.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_twitter():
    tapi = getattr(g, '_twitter', None)
    if tapi is None:
        tapi = g._twitter = twitter.create_twitter('twitter_config.json')
    return tapi

def get_bom():
    bom = getattr(g, '_bom', None)
    if bom is None:
        bom = g.bom = botometer.Botometer(
            mashape_key=json.load(open('mashape.json', 'r'))['mashape'],
            **json.load(open('twitter_config.json', 'r')))
    return bom

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug

    # blueprints!
    from fnd.main import main_blueprint
    app.register_blueprint(main_blueprint)

    @app.teardown_appcontext
    def close_db_conn(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return app
