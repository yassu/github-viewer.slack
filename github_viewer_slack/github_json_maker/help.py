#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from slackbot.bot import respond_to
from utils import COMMAND_TO_HELP


@respond_to('^\s*help(\s+\S+)?\s*$', re.IGNORECASE)
def help(message, command_name):
    if command_name is None:
        help_str = get_help_without_argument()
    else:
        command_name = command_name.strip()
        help_str = get_help_with_argument(command_name)
    message.reply(help_str)


def get_help_without_argument():
    help_str = '\n'
    for _, help_ in COMMAND_TO_HELP.items():
        help_str += '* {}\n'.format(help_)
    return help_str


def get_help_with_argument(command_name):
    help_str = ''
    if command_name in COMMAND_TO_HELP:
        help_str = COMMAND_TO_HELP[command_name]
    else:
        help_str = '{} is not used.'.format(command_name)
    return help_str
