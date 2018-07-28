#!/usr/bin/python

""" Here we can download the code and run our application, or whatever we want

    Problems found:
        Why the file I created in the VM using this cloud-init is not restored 
        when I create another VM from a Snapshot or reattach the Disk? 
"""

file = open("/home/ubuntu/testfile.txt", "w") 
file.write("hello world!") 
file.close() 
