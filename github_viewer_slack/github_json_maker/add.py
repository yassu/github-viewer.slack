#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen
from urllib.error import HTTPError
from slackbot.bot import respond_to
import re
import sys
from github_json_maker.utils import get_last_commit_id, get_commits


JSON_FILENAME = 'commits.json'


@respond_to('^\s*add\s+(\S+)\s*$', re.IGNORECASE)
def add(message, github_url):
    text = message.body['text']
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


class RegisteredRepositoryException(Exception):
    """
    そのリポジトリが既に登録されているときに検出されるException
    """

class NotFoundRepositoryException(Exception):
    """
    そのリポジトリがgithub上に存在しないときに検出されるException
    """


def add_repo(user_name, repo_name):
    d = dict()
    with open(JSON_FILENAME) as jf:
        d = json.load(jf)

    commit_id = get_last_commit_id(user_name, repo_name)

    if user_name not in d:
        d[user_name] = dict()
    if repo_name not in d[user_name]:
        d[user_name][repo_name] = commit_id
    else:
        raise RegisteredRepositoryException(
            '{}/{}は既に登録されています'.format(user_name, repo_name))

    with open(JSON_FILENAME, 'w') as jf:
        json.dump(d, jf, indent=4)
