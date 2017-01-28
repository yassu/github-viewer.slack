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


class RegisteredRepositoryException(Exception):
    """
    Exception that raise when the repository is already registered
    """

class NotFoundRepositoryException(Exception):
    """
    Exception that raise when there isn't the repository on the github
    """


def get_date_string():
    now = datetime.now()
    year, mon, day = now.year, now.month, now.day
    hour, minute, second = now.hour, now.minute, now.second
    return ("{} {}/{} {}:{}:{}\n".format(year, mon, day, hour, minute, second))


def my_log(text, filename=LOG_FILENAME):
    with open(filename, 'a') as f:
        f.write(get_date_string())
        f.write(text)
        f.write('\n')


def my_error_log(text, filename=ERROR_LOG_FILENAME):
    my_log('Error is occured:\n' + text, filename=filename)


def raise_registered_repository_exception(user_name, repo_name):
    raise RegisteredRepositoryException('{}/{} is already registered.'.format(
        user_name, repo_name))


def raise_not_found_repository_exception(user_name, repo_name):
    raise NotFoundRepositoryException('{}/{} is not found.'.format(
        user_name, repo_name))


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
        raise_not_found_repository_exception(user_name, repo_name)
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
    create series such as (commit_id, commit_message) for posting message
    """
    posted_last_commit_id = get_jdata()[user_name][repo_name]
    commits = get_commits(user_name, repo_name)

    for commit in commits:
        sha = commit['sha']
        if sha == posted_last_commit_id:
            break
        yield commit
