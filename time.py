#!python3
import datetime

name = input("What is your name?")

print("Would you like to know the current time," + name + "?")
ans = input()

if ans == 'y' or 'yes':
    today = datetime.datetime.now()
    print("The current time is, ", str(today))

else:
     print("Goodbye")
       
