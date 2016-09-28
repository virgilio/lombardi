# -*- coding: utf-8 -*-
from config import SLACK_USER as user

class Middleware():

    def __init__(self, sc):
        self.sc = sc

    def process_message(self, message):
        if message.has_key("user") and message["user"] == user:
            return None

        obj = type('obj', (object,), {})

        if message.has_key("text"):
            obj.message = message["text"]
        else:
            obj.message = str(message)

        result = obj()

        options = type('options', (object,), {})
        if message.has_key("channel"):
            print message["channel"]
            options.channel = message["channel"]
        else:
            options.channel = "#polanco"

        result.options = options

        return result

    def send_message(self, message, options):
        self.sc.api_call("chat.postMessage", as_user="true:", channel=options.channel, text=message)

    def send_file(self, message, filename, options):
        pass
