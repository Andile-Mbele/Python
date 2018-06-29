#!python3

yn = input('Continue? Yes or No:')
yn = yn.lower()

if yn[0] == 'y':
    print('You typed Yes')

elif yn[0] == 'n':
    print('You typed No')
        
elif yn == 'spam':
    print('What are you doing?')
            
else:
    print("You did not give any valid input.")
            
