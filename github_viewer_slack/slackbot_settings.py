#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

API_TOKEN = json.load(open('./../config.json'))['API_TOKEN']

default_reply = "Error: 文法の解釈に失敗しました"
