#!python3
#characterCount.py

message = '''I am Andy, the Zen of Xerox. My aspirations are
to be a force to be reckoned with.'''

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)    
