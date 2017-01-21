#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from slackbot.bot import respond_to
from github_json_maker.utils import get_commits


@respond_to('^\s*list\s*$', re.IGNORECASE)
def list(message):
    message.reply('listk')
