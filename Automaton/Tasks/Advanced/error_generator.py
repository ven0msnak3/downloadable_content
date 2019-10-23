def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()

# You can also generate errors this way:

try:
    something()
except error:
    raise Exception("Received an error message, but exited the program gracefully.")
