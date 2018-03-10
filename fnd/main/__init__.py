from flask import Blueprint
from jinja2 import TemplateNotFound

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='../templates/')

from . import routes

