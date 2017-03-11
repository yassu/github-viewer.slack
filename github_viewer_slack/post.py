#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slackbot_settings import Channel
from slackbot_settings import API_TOKEN, COMMITS_JSON_FILENAME, TRACEBACK_LIMIT
from slacker import Slacker
from utils import (
    get_jdata, get_post_commits, get_branches, my_error_log)
import traceback
import json


def post(**blob):
    query = {
        'as_user':      True,
        'text':         None,
        'username':     None,
        'parse':        None,
        'link_names':   None,
        'attachments':  None,
        'unfurl_links': None,
        'unfurl_media': None,
        'icon_url':     None,
        'icon_emoji':   None
    }
    query.update(blob)
    slacker = Slacker(API_TOKEN)
    slacker.chat.post_message(Channel, **query)


def post_by_repo(user_name, repo_name):
    commits = list(get_post_commits(user_name, repo_name))
    if len(commits) == 0:
        return

    attachment_list = []
    text = "%s/%s is comitted\n" % (user_name, repo_name)
    for commit in get_post_commits(user_name, repo_name):
        commit_link = '<' + commit['html_url'] + '|' + commit['sha'][0:6] + '>'
        message = commit['commit']['message'].split("\n", 1)[0][0:49]
        attachment_list.append(commit_link + ': ' + message)

    attachment_text = "\n".join(list(map(lambda x: "- " + x, attachment_list)))
    attachments = '[{"text": "%s"}]' % attachment_text
    post(text=text, attachments=attachments)

    last_commit_sha = commits[0]['sha']
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
