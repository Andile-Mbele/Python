#!python3
import os
import sys

print('What is your name?')
name = sys.stdin.readline()
while name == 'Andile':
    print('Access Granted')
    print('What do you want to do on this laptop ' + name + '?')

want = input()

while True:

    if want != 'work' or 'read' or 'study' or 'watch a movie':
        print('Bye')
    exit()
    

else:
    print('Alright, before we grant you access input the passcode first.')
    passcode = input()
if passcode != 'sparrow':
    print('Access Denied')
    print('You messed up the passcode, now the program is running na  infinite loop.')
    print('To close this, close the shell by clicking on the top right corner or simply press Ctrl-C to stop the loop')
else:
       print('Access Granted')

