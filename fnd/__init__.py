from flask import Flask

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug

    # blueprints!
    from fnd.main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
