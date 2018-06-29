#!python3
#!C:\Users\Andile XeroxZen\AppData\Local\Programs\Python\Python36\MyScripts

#This is a simple Python script that prompts the user

while True:
    print('Hello stranger, what is your name?')
    name = input()
    if name != 'Andile':
        continue
    print('Hello Andile. What is the password?')
    password =input()
    if password == 'lemonade':
        print('Access Granted')
        exit()
else:
    print('Access Denied')
