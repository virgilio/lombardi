# -*- coding: utf-8 -*-
import importlib, re

class Bot():
    ROUTES = []

    def __init__(self, client):
        from config import MODULES, MIDDLEWARE
        for m in MODULES:
            module = importlib.import_module(m)
            self.ROUTES += [route + (module,) for route in module.ROUTES]

        middleware = importlib.import_module(MIDDLEWARE)
        self.middleware = middleware.Middleware(client)

    def _process_message(self, message):
        return self.middleware.process_message(message)

    def _choose_response(self, message):
        for route in self.ROUTES:
            if "Oi" in str(message):
                return route
        return (None, None, None, None)

    def _send_message(self, message, options):
        if hasattr(self.middleware, 'send_message') and \
            callable(self.middleware.send_message):
            self.middleware.send_message(message, options)
        else:
            print "I don't know how to send messages =( " + str(message)

    def handle_message (self, payload):
        payload = self._process_message(payload)
        if payload is None:
            return False

        (regex, what_to_answer, what_to_do, module) = \
            self._choose_response(payload.message)
        if module is not None:
            ans = getattr(module, what_to_answer)
            if callable(ans):
                response = ans(payload.message)
                self._send_message(response, payload.options);
            else:
                print what_to_answer

            act = getattr(module, what_to_do)
            if callable(act):
                ok = act(payload.message, self)
                if not ok:
                    self._send_message("FUdeu")
            else:
                print what_to_do
        else:
            print "no module found"
