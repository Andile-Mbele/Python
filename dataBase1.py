#! python3
# A program to store information like in a database

n1 = ['Andile Mbele', 20, 'Systems Developer', 30000]
n2 = ['Jaden Scott', 21, 'Network Administrator', 28000]

people = [n1, n2]

for data in people:
    print(data)

for payIncr in people:
    print(payIncr[0].split()[-1])
    payIncr[3] *= 1.20

    for payIncr in people:
        print(payIncr[3])
        
