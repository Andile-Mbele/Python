#!python3

forms = ['mineral', 'animal', 'vegetable']
answer = input('Are you a mineral, animal or vegetable? \n')

if answer == forms[0]:
    print("You are a mineral. I bet you must be water.")

elif answer == forms[1]:
    print("You are an animal. Let's hope you are white meat.")

elif answer == forms[2]:
    print("YOu are a vegetable. Hmmm you are healthy.")

else:
    print("You did not give a valid answer.")
        
