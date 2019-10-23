# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:57:59 2018

@author: tariq
"""

import os
import shutil
sourcepath = r'Source File Path'
sourcefiles = os.listdir(sourcepath)
destinationpath = r'Destination File Path'
for file in sourcefiles:
    if file.endswith('.extension'):
        shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath,file))
