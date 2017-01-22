#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

CONFIG_FILENAME = './../config.json'
COMMITS_JSON_FILENAME = 'commits.json'
API_TOKEN = json.load(open(CONFIG_FILENAME))['API_TOKEN']
Channel = 'github'

PLUGINS = [
    'github_json_maker',
]

default_reply = "Error: 文法の解釈に失敗しました"
