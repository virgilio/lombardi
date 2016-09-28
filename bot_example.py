from lombardi import Bot
from config import SLACK_TOKEN as token

bot_example = Bot()

#try:
from slackclient import SlackClient

sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        msg = sc.rtm_read()
        if len(msg) > 0:
            print msg
            bot_example.handle_message(msg)
#except Exception:
#    print("Oh noes =(")
#    print Exception
