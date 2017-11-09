# -*- coding: utf-8 -*-
"""
Spyder Editor

Accepts 2 strings fname, lname and 
Prints them in reverse order lname followed by fname
"""

fname = input("What is your first name?")
lname = input("What is your last name?")
print("{0} {1}".format(lname,fname))
name = lname + " " + fname
print(name)