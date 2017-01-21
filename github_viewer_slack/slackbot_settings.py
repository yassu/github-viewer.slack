#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

CONFIG_FILENAME = './../config.json'
API_TOKEN = json.load(open(CONFIG_FILENAME))['API_TOKEN']

PLUGINS = [
    'github_json_maker',
]

default_reply = "Error: 文法の解釈に失敗しました"
