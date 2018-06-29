#! python3

fmenu = {'2 piecer' : 2.90, '3 piecer' : 3.50, 'Russian and Chips' : 3.00, 'Plain Chips' :
         1.00, 'juice' : 1.30}

order = input("What will you be having today?: \n2 piecer \n3 piecer \nRussian and Chips \nPlain Chips \nJuice: \n\n")

if order == '2 piecer':
    print("That will be", "$", "%.2f" % fmenu.get("2 piecer"))

elif order == '3 piecer':
    print("Total price for 3 piecer is", "$", "%.2f" % fmenu.get('3 piecer'))

elif order == 'Russian':
    print("Total price for Russian sausage is", "$", "%.2f" % fmenu.get('Russian and Chips'))

elif order == 'Plain Chips':
    print("Price for plain chips", "$", "%.2f" % fmenu.get('Plain Chips'))

elif order == 'juice':
    print("The price for juice is", "$", "%.2f" % fmenu.get('juice'))

else:
    print("There is no information for " + order)
    print("What is it's price?")
    #fprice = int(input())
        #fname = input("What is the food name?")
        #fprice = int(input("What is the price of that food name?"))
        
    addMenu = input()
    fmenu[order] = addMenu 
    #fmenu.update(fprice)

    print("The food menu has been updated.")

