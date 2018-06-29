# to be run form the shell

while True: #Risk of running an infinte loop.
    char = input("Enter a string of at least 4 characters, or q to quit the program.: \n")
    if char == 'q':
        break
    if len(char) < 4:
        print("Value is too small.")
        continue

    print("The string you entered was of sufficient length")
    raise SystemExit #To prevent an infinite loop.
    
