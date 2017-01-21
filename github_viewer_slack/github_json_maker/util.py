#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slackbot.bot import respond_to
import re


@respond_to('^\s*list\s*$', re.IGNORECASE)
def add(message):
    message.reply('list')
