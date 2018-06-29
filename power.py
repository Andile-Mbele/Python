#! python3
'''
Author: Andile Mbele
Module: power.py
'''

ui = input("Enter a number: ")
print("The data type is originally", (type(ui)))
uconv = int(ui)
print("Now the d.t. is", (type(uconv)))
power = uconv ** 8
print(ui, "raised to the 8th power is: ", power)
