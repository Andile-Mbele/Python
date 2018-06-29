#!python3

friendNames = [ ]
while True:
    print('Enter the name of the friend ' + str(len(friendNames) + 1) +
          ' (or enter nothing to stop.')
    name = input()
    if name == ' ':
        break
    friendNames = friendNames + [name] # list concatenation(joining)

    print('The friend names are:')
    for name in friendNames:
        print('    ' + name)
