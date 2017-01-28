#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from slackbot.bot import respond_to
import re
import traceback
from slackbot_settings import COMMITS_JSON_FILENAME, TRACEBACK_LIMIT
from utils import (get_last_commit_id, my_error_wrap, my_error_log,
    RegisteredRepositoryException, NotFoundRepositoryException)


@respond_to('^\s*(add\s|\+)\s*(\S+)\s*$', re.IGNORECASE)
@my_error_wrap()
def add(message, _, github_url):
    if len(github_url.split('/')) != 2:
        my_error_log("{}.split('/') != 2".format(github_url))
        message.reply('Illegal as github repository')
        return
    user_name, repo_name = github_url.split('/')
    try:
        add_repo(user_name, repo_name)
        message.reply("Repository {}/{} is registered.".format(
            user_name, repo_name))
    except RegisteredRepositoryException as ex:
        my_error_log(traceback.format_exc(TRACEBACK_LIMIT))
        message.reply("Error: {}".format(ex.args[0]))
    except NotFoundRepositoryException as ex:
        my_error_log(traceback.format_exc(TRACEBACK_LIMIT))
        message.reply("Error: {}".format(ex.args[0]))



def add_repo(user_name, repo_name):
    d = dict()
    with open(COMMITS_JSON_FILENAME) as jf:
        d = json.load(jf)

    commit_id = get_last_commit_id(user_name, repo_name)

    if user_name not in d:
        d[user_name] = dict()
    if repo_name not in d[user_name]:
        d[user_name][repo_name] = commit_id
    else:
        raise RegisteredRepositoryException(
            '{}/{} is already registered.'.format(user_name, repo_name))

    with open(COMMITS_JSON_FILENAME, 'w') as jf:
        json.dump(d, jf, indent=4)
