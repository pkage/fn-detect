from flask import render_template, request, jsonify
from .. import get_twitter, get_bom
from jinja2 import TemplateNotFound
from . import main_blueprint
from ..data import twitter
import arrow
import json
import math

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/dox/start')
def doxstart():
    return render_template('doxstart.html')

@main_blueprint.route('/dox/load/<uname>')
def load_dox(uname):
    return render_template('loading.html', username=uname)

@main_blueprint.route('/dox/username/<uname>', methods=['POST', 'GET'])
def dox_user(uname):
    if request.method == 'POST':
        username = request.form['username']
    else:
        username = uname
    if username[0] == '@':
        username = username[1:]

    api = get_twitter()
    user = twitter.get_user(api, username)
    tweets = twitter.get_tweets(api, username, batches=3, exclude_replies=True)
    print('{} tweets scanned'.format(len(tweets)))
    graphs = twitter.analyze_tweets(tweets)
    days_old = (arrow.utcnow() - twitter.get_created_at(user)).days
    sample = {
        'size': len(tweets),
        'oldest': twitter.get_created_at(tweets[-1]).humanize(),
        'tweets_per_day': math.floor(user.statuses_count / days_old),
        'days_old': days_old
    }

    bom = get_bom()
    results = bom.check_account(username)
    print(results)

    def grade(num):
        if num > 0.66:
            return 'is-danger'
        elif num > 0.33:
            return 'is-warning'
        return 'is-success'

    def interpret(num):
        if num > 0.66:
            return 'probably a bot'
        elif num > 0.33:
            return 'may be a bot'
        return 'probably not a bot'

    return render_template('doxshow.html', username=username, user=user, bom=results, graphs=graphs, grade=grade, interpreted_score=interpret(results['scores']['english']), sample=sample)


@main_blueprint.route('/api/dox/<username>')
def api_dox(username):
    bom = get_bom()
    results = bom.check_account(username)
    return jsonify(results)
