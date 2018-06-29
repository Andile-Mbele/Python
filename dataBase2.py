#! python3
# A program to store information like in a database


NAME, AGE, JOB, SALARY = range(4)

# variables representing individuals
n1 = ['Andile Mbele', 20, 'Systems Developer', 30000] 
n2 = ['Jaden Scott', 21, 'Network Administrator', 28000]


# combining the above variables
people = [n1, n2]

print(people, '\n')

#appending the people variable
people.append(['Nick Zeal', 25, 'Technician', 25000])

#iterating through the data
for data in people:
    print(data, '\n')     # to print all the data presented in 'people'

for payIncr in people:
    print(payIncr[0].split()[0], '\n')
    payIncr[SALARY] *= 1.20         #increasing salary by 20%

    for payIncr in people:
        print(payIncr[SALARY], '\n')  #to display the final salary.
        
