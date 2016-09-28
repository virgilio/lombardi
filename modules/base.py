# -*- coding: utf-8 -*-
ROUTES = [
    (u"^u[hu]+", "default_response", "default_work"),
    (u"u[hu]+", "default_response", "default_work"),
    (u"mah oe", "default_response", "default_work"),
    (u"não pode", "default_response", "default_work"),
    (u"^batema*", "batema_response", "default_work"),
    (u"Batema, seu bicha, seu puto", "default_response", "default_work")
]

def default_response(message):
    print "base: default response"
    if message == "uhuhuhuhu":
        return "Vou comer a tia do batema"
    else:
        return message

def default_work(bot, message):
    print "base: default work"
    _default_work_private(message)

    return True

def batema_response(message):
    return "Você não é aquele viadinho não?"

def _default_work_private(message):
    pass
