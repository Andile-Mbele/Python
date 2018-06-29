#!python3
#! /usr/bin/python3

'''
Module : keyboardInput.py
Author : Andile Mbele
Contact : andilembele001@gmail.com
Date : 2 April 2018
'''

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

print("\nYou entered {0} as your lower bound, and you entered {1} as your \
upper bound." .format(lb, ub))
verif = input("\nProceed y/n: ")
response = verif.lower()

if response == "y":
    for multiplier in range (lb, (ub + 1)):
        for i in range (1, 21):
            print(i, "x", multiplier, "=", i * multiplier)

else:
    print("We're done")
