#!python3
#birthday.py


# birthday info stored in a dictionary{}
birthdays = {'Andile' : '3 December', 'Mzie' : '22 February',
            'Tumelo' : '18 November', 'Glenda' : '25 November',
            'Princess' : '7 May', 'Mama' : '15 July', 'Tata' :
            '18 July', 'Lindani' : '12 February', 'Hellen' :
            '12 December', 'Dalindyebo' : '10 April', 'Nokukhanya' :
            '1 January'
    }

while True:
    print('Enter a name: ')  #inputs name or blank to quit.
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is ' + name + '\'s birthday')
    else:
        print('There is no birthday information for ' + name)
        print('What is their birth date?')
        bday = input()
        birthdays[name] = bday
        #birthdays.update(name.bday)
        print('Birthday database updated.')
    
        
