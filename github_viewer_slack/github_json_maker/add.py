#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import re

@respond_to('add', re.IGNORECASE)
def add(message):
    text = message.body['text']
    message.reply('You send "{}"'.format(text))
