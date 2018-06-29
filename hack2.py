#!python3
#infinite loop

import os

#print("What is your username? \n")
UsrName = str(input("Enter a valid username? \n"))

if UsrName != 'Andile' or 'AJ' or 'andile':
    print("Entered Username is not valid")
    
#OpenSysInfo = SysInfoFile.read()
passcodeFile = open('C:/txtfiles/SecretPassword.txt') 
SecretPasscode = passcodeFile.read()
#print("What is your user passcode? \n")
typedPasscode = input("What is your user passcode? \n")

while True:
    if typedPasscode == SecretPasscode:
        print("Running a systems analysis and diagnosis. Don't switch off the computer.           System Architecture under attack. Take necessary steps.     101010100101010101010101010101010 \n" * 10)
        print("1       0        1      0        1        0        1         0          1          0      1       0      1       0       1     0    1       0       1        0        1        0     1    0    1" * 10)
        print("Hacker Wars :: codenamed by Andile.           Hacker style Xerox Code, the Hack 2.0 Initiated.         1010101010101010101010101010101010100101010101010100 \n" * 3)

        SysInfoFile = open('C:/txtfiles/system_info.txt')
        print('\n', SysInfoFile.readlines(), '\n',)

    elif typedPasscode == 'abcde' or '12345':
        print("That's the dumbest security access combination")

    else:
        print("Access Denied")
    
