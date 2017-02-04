#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from slackbot.bot import respond_to
from slackbot_settings import COMMITS_JSON_FILENAME, TRACEBACK_LIMIT
from utils import COMMAND_TO_HELP

@respond_to('^\s*help\s+(\S+)\s*$', re.IGNORECASE)
def help(message, command_name):
    help_str = ''
    if command_name in COMMAND_TO_HELP:
        help_str = COMMAND_TO_HELP[command_name]
    else:
        help_str = '{} is not used.'.format(command_name)
    message.reply(help_str)
