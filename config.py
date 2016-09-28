# -*- coding: utf-8 -*-
MIDDLEWARE_ROOT = "middlewares"
MODULE_ROOT = "modules"

MODULES = [
    "base",
    "extended",
]

SLACK_TOKEN = ""
SLACK_USER = ""

MODULES = (".".join([MODULE_ROOT, m]) for m in MODULES)
MIDDLEWARE = ".".join([MIDDLEWARE_ROOT, "slack"])
