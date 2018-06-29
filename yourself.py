#python3.6

'''
Author: Andile Mbele
Name: Yourself.py
Date: 12 February
'''
while True:
    print ('Hey stranger, what is your name?')
    name = input()
    if name != 'Andile':
        print('Access Denied')
    else:
        print('Access Granted.')
        print ('\nHello ' + name + ' so how old are you?')
        age = input()
        print('So when exactly is your birthday?')
        birthday = input()
        print('What do you do for a living?')
        living = input()
        print('What are your life aspirations?')
        aspirations = input()    
    
    if aspirations <= str(len(5)):
        print('Not sufficient enough. Try again')
        again = input()
        print('There you go, all the best in your dreams')

    else:
        print('Cool aspirations ' + name + ' . All the best.' )
            
response = input()
print('''Thank you for taking your time and  doing this, now the system
         is aware of your earthly existence.''')
    


