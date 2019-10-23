import os
import shutil
for filename in os.listdir():
    if filename.endswith('your file type'):
        #os.unlink(filename)
        #shutil.rmtree(foldername)
        print(filename)
        print(foldername)

# The os.unlink line and the shutil.rmtree line are commented out
# This is done for your computer's safety as these are permanent deletion methods
