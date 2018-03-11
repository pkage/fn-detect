#! /usr/bin/env python

import json
import botometer

def check_account(username):
    bom = botometer.Botometer(
        mashape_key=json.load(open('../mashape.json', 'r'))['mashape'],
        **json.load(open('../twitter_config.json', 'r')))

    return bom.check_account(username)

if __name__ == '__main__':
    print(check_account('@irissasara'))
