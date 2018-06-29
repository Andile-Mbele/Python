#!python3
# pw.py -A almost secure password locker program.

import sys
PASSWORDS ={'private' : 'name01',
                             'Gmail1' : 'rosnet@955',
                             'Gmail2' : 'infiniteloop2000',
                             'Yahoo' : 'Dun**no',
                             'iTunes' : 'Ros500cv./',
                             'Adobe Reader' : 'Ros500cv./',
                             'Hackline' : 'say#',
                            'Wikipedia' : '***0**m',
                            'HubPages' : 'forgotten',
                            'Facebook' : 'spider==man',
                           'Twitter' : 'rememberFBold',
                           'Bcom' : 'rock320pS@',
                           'Soundcloud' : 'zealot101',
                           'Optrex' : 'mbcQ***@/.co',
                            'hubpages' : 'loess400$%'
                            'Wordpress' : 'loess400$%',
                            'Spotify' : 'Rsvp*000'
                            'mySite' : 'infiniteloop@245'}

if len(sys.argv) < 2:
    print(Usage: python pw.py [account] - copy account password)
    sys.exit()

    account = sys.argv[1] # first command line arg is the account name

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS [account])
        print('Password for ' + account + 'copied to the clipboard.')
        else:
            print('There is no account named ' + account)
