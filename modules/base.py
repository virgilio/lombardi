# -*- coding: utf-8 -*-
ROUTES = [
    (r'*', "default_response", "default_work"),
    (r'mah oe', "default_response", "default_work")
]

def default_response(message):
    print "base: default response"
    return message

def default_work(bot, message):
    print "base: default work"
    _default_work_private(message)

    return True

def _default_work_private(message):
    pass
