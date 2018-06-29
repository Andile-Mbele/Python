#!python3

import datetime as dt

name = input("What is your name?")
age = input("How old are you?")
age2days = int(age) * 365

birth_gift = input("What is your most preferable and yet affordable birthday present?")

bday = dt.datetime.now() - dt.timedelta(days = age2days)
conv = int(100) * int(365)
calc =bday + dt.timedelta(days = conv)
output = calc.strftime('%Y')

print("Fun fact {}, did you know you be 100 years old in {}" .format(name, output))

