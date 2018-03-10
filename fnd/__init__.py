from flask import Flask, g
import sqlite3

DATABASE = '../scraper/fn-detect.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

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
