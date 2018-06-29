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

bdayRes = birthdays.update({'Rejoice' : '26 March',
                                    'Thembeka' : '23 November'})
#print(len(bdayRes))

while True:
    print('Enter a name: ')  #inputs name or blank to quit.
    name = input()
    name
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is ' + name + '\'s birthday')
             
    elif subject in bdayRes:
        print(birthdays[name] + ' is ' + name + '\'s birthday')        
        #birthdays.update(name.bday)       
    else:
        print('There is no information on ' + name)
        break
    
    #DoThis = birthdays.values()
    #DoThat = birthdays.keys()

    #print((str(DoThis)))
    #print((str(DoThat)))
        #print('Birthday database updated.')
        
#while True:
#    print('Enter a name: ')  #inputs name or blank to quit.
#    name = input()
#    if name == '':
#        break

    
    
        
