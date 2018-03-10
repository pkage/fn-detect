from flask import render_template, abort
from jinja2 import TemplateNotFound
from . import main_blueprint

@main_blueprint.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
