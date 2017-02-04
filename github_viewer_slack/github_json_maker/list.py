#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from slackbot.bot import respond_to
from utils import get_commits, get_branch_names, my_error_wrap


@respond_to('^\s*list(\s+\S+)?\s*$', re.IGNORECASE)
@my_error_wrap()
def list(message, pattern):
    if pattern is None:
        pattern = '.*'
    pattern = pattern.strip()
    print(pattern)

    text = "branch names\n"
    for branch_name in get_branch_names():
        if re.search(pattern, branch_name):
            text += "* {}\n".format(branch_name)
    message.reply(text)
