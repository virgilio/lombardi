def process_message(message):
    obj = type('obj', (object,), {})
    obj.message = message
    obj.options = None
    return obj()

def send_message(message, options):
    pass
