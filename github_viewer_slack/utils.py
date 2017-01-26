#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from datetime import datetime
import functools
import traceback
import json
from slackbot_settings import LOG_FILENAME, ERROR_LOG_FILENAME, TRACEBACK_LIMIT
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_date_string():
    now = datetime.now()
    year, mon, day = now.year, now.month, now.day
    hour, minute, second = now.hour, now.minute, now.second
    print(hour)
    return ("{} {}/{} {}:{}:{}\n".format(year, mon, day, hour, minute, second))


def my_log(text, filename=LOG_FILENAME):
    with open(filename, 'a') as f:
        f.write(get_date_string())
        f.write(text)
        f.write('\n')


def my_error_log(text, filename=ERROR_LOG_FILENAME):
    my_log('Error is occured:\n' + text, filename=filename)


def my_error_wrap(filename=ERROR_LOG_FILENAME):
    def _my_error_wrap(func):
        @functools.wraps(func)
        def command_func(*args, **kw):
            try:
                return func(*args, **kw)
            except Exception as ex:
                with open(filename, 'a') as f:
                    f.write(get_date_string())
                    f.write('Error is occured:\n')
                    traceback.print_exc(TRACEBACK_LIMIT, f)
                    f.write('\n')
        return command_func
    return _my_error_wrap


@my_error_wrap()
def hello():
    print('hello')
    0/0


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
    data = response.decode()
    return json.loads(response.decode())


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


def get_post_commits(user_name, repo_name):
    """
    postする (commit_id, commit_message) の列を生成
    """
    posted_last_commit_id = get_jdata()[user_name][repo_name]
    commits = get_commits(user_name, repo_name)

    for commit in commits:
        sha = commit['sha']
        if sha == posted_last_commit_id:
            break
        yield commit


class RegisteredRepositoryException(Exception):
    """
    そのリポジトリが既に登録されているときに検出されるException
    """

class NotFoundRepositoryException(Exception):
    """
    そのリポジトリがgithub上に存在しないときに検出されるException
    """
