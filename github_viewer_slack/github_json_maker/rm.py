#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import json


@respond_to('^\s*rm\s+(\S+)\s*')
def rm(message, github_url):
    message.reply("rm message")
