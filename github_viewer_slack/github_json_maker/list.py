#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from slackbot.bot import respond_to
from utils import get_commits, get_branch_names


@respond_to('^\s*list\s*$', re.IGNORECASE)
def list(message):
    text = "branch names\n"
    for branch_name in get_branch_names():
        text += "* {}\n".format(branch_name)
    message.reply(text)
