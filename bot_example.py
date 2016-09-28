# -*- coding: utf-8 -*-
from lombardi import Bot
from config import SLACK_TOKEN as token
from slackclient import SlackClient

sc = SlackClient(token)

bot_example = Bot(sc)

#try:
if sc.rtm_connect():
    while True:
        msg = sc.rtm_read()
        if len(msg) > 0:
            print msg
            bot_example.handle_message(msg[0])
#except Exception:
#    print("Oh noes =(")
#    print Exception
