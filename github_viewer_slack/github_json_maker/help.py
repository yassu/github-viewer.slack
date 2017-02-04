#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from slackbot.bot import respond_to
from slackbot_settings import COMMITS_JSON_FILENAME, TRACEBACK_LIMIT

@respond_to('^\s*help\s+(\S+)\s*$', re.IGNORECASE)
def help(message, command_name):
    message.reply('help command')
