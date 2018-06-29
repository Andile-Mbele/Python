val1 = input("Enter a str element 1/3: ")
val2 = int(input("Enter an int element 2/3: "))
val3 = float(input("Enter a float element 3/3: "))

lst = [val1, val2, val3]
tpl = (val1, val2, val3)
dict = {"First element ": val1, "Second element ": val2,
        "Third element ": val3}

print("\n")
print("Here is the list: ", lst)
print("Here is the tuple: ", tpl)
print("Here is the dictionary: ", dict)

print('\n')
val4 = input("Enter another list string element: ")
lst.append(val4)
print("Here is your updated list: ", lst)
