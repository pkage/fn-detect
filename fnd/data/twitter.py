#! /usr/bin/env python

import json
import arrow
import twitter

def create_twitter(cfg):
    if type(cfg) is str:
        with open(cfg, 'r') as cfgfile:
            cfg = json.load(cfgfile)

    return twitter.Api(
        consumer_key=cfg['consumer_key'],
        consumer_secret=cfg['consumer_secret'],
        access_token_key=cfg['access_token_key'],
        access_token_secret=cfg['access_token_secret'],
        tweet_mode='extended'
    )

def get_user(api, username):
    return api.GetUser(screen_name=username)

def get_tweets(api, username, batches=3, exclude_replies=False):
    def fetch(max_id=None):
        statuses = api.GetUserTimeline(screen_name=username, count=200, exclude_replies=exclude_replies)
        return [t for t in statuses]

    earliest = None
    tweets = []
    for b in range(batches):
        tweets += fetch(earliest)
        earliest = tweets[-1].id

    return tweets

def get_created_at(tweet):
    return arrow.get(tweet.created_at, 'ddd MMM DD HH:mm:ss Z YYYY')


def analyze_tweets(tweets):
    # time heatmap
    timemap = {
        'Sun': [],
        'Mon': [],
        'Tue': [],
        'Wed': [],
        'Thu': [],
        'Fri': [],
        'Sat': []
    }

    for tweet in tweets:
        t = arrow.get(tweet.created_at, 'ddd MMM DD HH:mm:ss Z YYYY')
        timemap[t.format('ddd')].append(
            (int(t.format('HH')) * 60 * 60) +
            (int(t.format('mm')) * 60) +
            (int(t.format('ss')))
        )

    return {
        "timemap": timemap,
    }

if __name__=="__main__":
    api = create_twitter('../twitter_config.json')
    tweets = get_tweets(api, 'realDonaldTrump', batches=5)

    print('retrieved {} tweets for @{}'.format(
        len(tweets),
        'realDonaldTrump'
    ))

    # Sat Mar 10 20:02:02 +0000 2018
    print(arrow.get(tweets[0].created_at, 'ddd MMM DD HH:mm:ss Z YYYY'))
    print(analyze_tweets(tweets))
    # [print(t) for t in get_tweets(api, 'realDonaldTrump')]
