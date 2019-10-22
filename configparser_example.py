# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:49:16 2019

@author: tariq
"""

# This example shows the use of config parser module
# TODO: Start with importing the appropriate libraries

import configparser
import logging

# TODO: Define a function that reads a .ini file and saves the keys into respective containers

def con_figure():
    config = configparser.ConfigParser()
    config.read('code_file.ini')
    public = config['code']['public']
    private = config['code']['private']
    logging.info("Public key is: %s", public)
    logging.info("Private key is: %s", private)

# TODO: Initialize the function and run it with appropriate logging information
    
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Starting main...")
    con_figure() # TODO: Call the function within the 'if' statement because we didn't use init