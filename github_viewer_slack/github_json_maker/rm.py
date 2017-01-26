#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot_settings import COMMITS_JSON_FILENAME
from utils import NotFoundRepositoryException, my_error_wrap, my_error_log
import traceback
import json


@respond_to('^\s*(rm\s|remove\s|delete\s|-)\s*(\S+)\s*')
@my_error_wrap()
def rm(message, _, github_url):
    if len(github_url.split('/')) != 2:
        my_error_log("{}.split('/') != 2".format(github_url))
        message.reply('Illegal as github repository')
        return
    user_name, repo_name = github_url.split('/')
    try:
        delete_repo(user_name, repo_name)
    except NotFoundRepositoryException as ex:
        my_error_log(traceback.format_exc())
        message.reply('{}/{}は既に登録されています'.format(
            user_name, repo_name))
        return

    message.reply("{}/{} を削除しました".format(user_name, repo_name))


def delete_repo(user_name, repo_name):
    d = dict()
    with open(COMMITS_JSON_FILENAME) as jf:
        d = json.load(jf)
    try:
        del(d[user_name][repo_name])
    except KeyError:
        my_error_log(traceback.format_exc())
        raise NotFoundRepositoryException('{}/{}は既に登録されています'.format(
            user_name, repo_name))

    with open(COMMITS_JSON_FILENAME, 'w') as jf:
        json.dump(d, jf, indent=4)
