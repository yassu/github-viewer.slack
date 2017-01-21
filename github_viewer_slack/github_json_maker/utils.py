#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
import json


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
    except HTTPError:
        raise NotFoundRepositoryException('リポジトリ {}/{} は存在しません'
            .format(user_name, repo_name))
    data = response.decode()
    return json.loads(response.decode())

class RegisteredRepositoryException(Exception):
    """
    そのリポジトリが既に登録されているときに検出されるException
    """

class NotFoundRepositoryException(Exception):
    """
    そのリポジトリがgithub上に存在しないときに検出されるException
    """

