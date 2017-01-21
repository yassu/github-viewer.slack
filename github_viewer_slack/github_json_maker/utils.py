#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slackbot.bot import respond_to
import re


def get_last_commit_id(user_name, repo_name):
    data = get_commits(user_name, repo_name)
    if len(data) == 0:
        return ''
    else:
        return data[0]['sha']


def get_commits(user_name, repo_name):
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        user_name,
        repo_name)
    try:
        response = urlopen(url).read()
    except HTTPError as ex:
        raise NotFoundRepositoryException('リポジトリ {}/{} は存在しません'
            .format(user_name, repo_name))
    return json.loads(response.decode())
