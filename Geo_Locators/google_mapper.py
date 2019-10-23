# Your regular imports.

import webbrowser as wb
import sys
import pyperclip

# Code that lets you input your address when you input the name of this file
# into a terminal followed by your intended address.

if len(sys.argv) > 1:
    ADDRESS = ' '.join(sys.argv[1:])
else:
    ADDRESS = pyperclip.paste()

# The below line will open the google maps in the appropriate browser.
# This will also have your location set to the correct coordinates (hopefully).

wb.open('https://www.google.com/maps/place/' + address)
