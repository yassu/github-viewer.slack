#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slackbot_settings import Channel
from slackbot_settings import API_TOKEN, COMMITS_JSON_FILENAME, TRACEBACK_LIMIT
from slacker import Slacker
from utils import (get_jdata, get_commits, get_post_commits,
        get_branches, my_error_log)
import traceback
import json

def post(message):
   slacker = Slacker(API_TOKEN)
   slacker.chat.post_message(Channel, message , as_user=True)


def post_by_repo(user_name, repo_name):
    commits = list(get_post_commits(user_name, repo_name))
    if len(commits) == 0:
        return

    last_commit_sha = commits[0]['sha']
    text = "{}/{} is comitted: \n".format(user_name, repo_name)
    for commit in get_post_commits(user_name, repo_name):
        message = commit['commit']['message'].split("\n", 1)[0]
        text += "* {}\n".format(message)

    last_posted_sha = get_jdata()[user_name][repo_name]
    text += "https://github.com/{}/{}/compare/{}...master\n".format(
        user_name, repo_name, last_posted_sha)

    post(text)
    update_repo(user_name, repo_name, last_commit_sha)


def update_repo(user_name, repo_name, last_commit_sha):
    d = get_jdata()
    d[user_name][repo_name] = last_commit_sha
    with open(COMMITS_JSON_FILENAME, 'w') as jf:
        json.dump(d, jf, indent=4)


def main():
    for user_name, repo_name in get_branches():
        post_by_repo(user_name, repo_name)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        my_error_log(traceback.format_exc(TRACEBACK_LIMIT))
