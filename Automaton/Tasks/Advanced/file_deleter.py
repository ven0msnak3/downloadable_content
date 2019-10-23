import os

myfile = '/delicious/walnut/waffles/new_sonnet.txt'

if os.path.isfile(myfile):
    os.remove(myfile)
else:
    print("Error: %s file not found" % myfile)
