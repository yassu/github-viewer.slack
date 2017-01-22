#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from slackbot.bot import respond_to
import re
from slackbot_settings import COMMITS_JSON_FILENAME
from utils import (get_last_commit_id,
    RegisteredRepositoryException, NotFoundRepositoryException)


@respond_to('^\s*(add\s|\+)\s*(\S+)\s*$', re.IGNORECASE)
def add(message, _, github_url):
    if len(github_url.split('/')) != 2:
        message.reply('Illegal as github repository')
        return
    user_name, repo_name = github_url.split('/')
    try:
        add_repo(user_name, repo_name)
        message.reply("リポジトリ {}/{}を登録しました".format(
            user_name, repo_name))
    except RegisteredRepositoryException as ex:
        message.reply("Error: {}".format(ex.args[0]))
    except NotFoundRepositoryException as ex:
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
            '{}/{}は既に登録されています'.format(user_name, repo_name))

    with open(COMMITS_JSON_FILENAME, 'w') as jf:
        json.dump(d, jf, indent=4)
