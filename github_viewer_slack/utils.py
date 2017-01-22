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


def get_post_commits(user_name, repo_name):
    pass


def get_branches():
    for user_name, repos in get_jdata().items():
        for repo_name in repos:
            yield (user_name, repo_name)


def get_branch_names():
    for user_name, repo_name in get_branches():
        yield user_name + "/" + repo_name


def get_jdata():
    with open('commits.json') as jf:
        return json.load(jf)

class RegisteredRepositoryException(Exception):
    """
    そのリポジトリが既に登録されているときに検出されるException
    """

class NotFoundRepositoryException(Exception):
    """
    そのリポジトリがgithub上に存在しないときに検出されるException
    """
