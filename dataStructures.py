#!python3

S = [x ** 2 for x in range(10)]

def choice_a(x):
	print(S)
	return 

def choice_b(x):
	V = [2 ** i for i in range(x)]
	print(V)
	return

def choice_c(y):
	M = [x for x in range(y) if x % 2 == 0]
	print(M)

def choice_d():
	raise SystemExit()

print("Which operation do you want to perform? \n")

print('''
	a : x to power of 2.
	b : 2 to the xth power.
	c : the modular 2
	d : Quit
	''')

response = input("Choice: ")
response2 = int(input("Upper Values?"))

if response == 'a':
	choice_a(response2)

elif response == 'b':
	choice_b(response2)

elif response == 'c':
	choice_c(response2)

else:
        choice_d


