#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

CONFIG_FILENAME = './../config.json'
COMMITS_JSON_FILENAME = 'commits.json'
ERROR_LOG_FILENAME = 'log/error_log'
LOG_FILENAME = 'log/log'
TRACEBACK_LIMIT = 10
API_TOKEN = json.load(open(CONFIG_FILENAME))['API_TOKEN']
Channel = 'github'

PLUGINS = [
    'github_json_maker',
]

default_reply = "Error: Illegal syntax"
