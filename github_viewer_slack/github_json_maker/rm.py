#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import json


@respond_to('^\s*rm\s+(\S+)\s*')
def rm(message, github_url):
    if len(github_url.split('/')) != 2:
        message.reply('Illegal as github repository')
        return
    user_name, repo_name = github_url.split('/')
    message.reply("rm message")
