#!C:\Users\Andile XeroxZen\AppData\Local\Programs\Python\Python36\MyScripts
#! /usr/bin/python
import os

passwordFile = open('C:/txtfiles/SecretPassword.txt')
SecretPassword = passwordFile.read()
print("Enter your password.")
typedPassword = input()
if typedPassword == SecretPassword:
    print('Access Granted')
    
elif typedPassword == '12345':
    print("That's a lame password used by duds")

else:
    print("Access Denied")

    #print("The password is ",)

#@py.exe 'C:\Users\samsung\AppData\Local\Programs\Python\Python36\MyScripts\passwordFile.py %*
#@pause    
