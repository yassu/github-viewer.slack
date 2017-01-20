#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import re

@respond_to('^\s*add\s+(\S+)\s*$', re.IGNORECASE)
def add(message, github_url):
    text = message.body['text']
    user_name, repo_name = github_url.split('/')
    message.reply('You send "{}"'.format(text))
