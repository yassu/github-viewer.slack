#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slackbot_settings import Channel
from slackbot_settings import API_TOKEN
from slacker import Slacker

def post(message):
   slacker = Slacker(API_TOKEN)
   slacker.chat.post_message(Channel, message , as_user=True)

if __name__ == '__main__':
    post('This is a test post.')
