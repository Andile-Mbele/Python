#!python3

import random
import sys
import os

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print ("There are %d types of people." %10)
print ("Those who know %s and those who %s.", binary, do_not)

print("I said: %r" %x)

print ("I also said: '%s." %y)

hilarious = "false"
joke_evaluation = "Isn't that joke so funny?! %r"

print ("joke_evaluation % hilarious")

w = "This is the left side of... %r"
e = "a string with a right side %s"

print ("w" + "e " )