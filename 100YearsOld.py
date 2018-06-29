#!python3

import datetime as dt

name = input("What is your name?")
age = input("How old are you?")
age2days = int(age) * 365

bday = dt.datetime.now() - dt.timedelta(days = age2days)
conv = int(100) * int(365)
calc =bday + dt.timedelta(days = conv)
output = calc.strftime('%Y')

print("Hie {} you will be 100 years old in {}" .format(name, output))

