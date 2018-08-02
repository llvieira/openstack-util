#!/usr/bin/python

""" 
Here we can download the code and run our application, or whatever we want.
"""

import os

# install git
os.system('sudo apt-get update')
os.system('sudo apt-get install git -y')

# create a file
file = open("/home/ubuntu/testfile.txt", "w") 
file.write("hello world!") 
file.close() 
