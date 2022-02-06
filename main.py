import salesModule
import PersonClass


storeList = ['Best Buy','Walmart','Target','Costco','Ralphs']

bestBuyList = {1:('Laptop',299.99), 2:('Gaming PC',1029.99),3:('TV',249.99),4:('Xbox One',219.99),5:('Nintendo Switch', 279.99)}

walmartList = {1:('Apple',2.99), 2:('Pie',9.99),3:('Juice',10.99),4:('Xbox One',219.99),5:('Nintendo Switch', 279.99)}

targetList = {1:('Levi jeans',22.99), 2:('Bedframe',199.99),3:('Shampoo',10.99),4:('Soap',2.99),5:('Gum', 5.99)}

costcoList = {1:('Water',4.99), 2:('Meat',25.99),3:('Chicken',23.99),4:('Sofa',219.99),5:('TV', 200.99)}

ralphsList = {1:('Grape',5.99), 2:('Tomato',1.99),3:('Yogurt',3.99),4:('Brocolli',3.99),5:('Milk', 3.99)}


print('These are our available stores to shop from.\n')

counter = 1 
for i in storeList:
  print(counter,')',i)
  counter += 1

print('\nWhich store would you like to shop from?')
print('*** Please enter the number correspending to the store ***')
while True:
   try:
      userInput = int(input('Your choice: '))
      if userInput >= 6 or userInput <= 0:
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again')

if userInput == 1:
  salesModule.printList(bestBuyList,storeList[0])

elif userInput == 2:
  salesModule.printList(walmartList,storeList[1])

elif userInput == 3:
  salesModule.printList(targetList,storeList[2])

elif userInput == 4:
  salesModule.printList(costcoList,storeList[3])

elif userInput == 5:
  salesModule.printList(ralphsList,storeList[4])

customerList = []

keepChoosing = 'Y'
while keepChoosing == 'Y':
  #choice = int(input('\nWhat is your choice: '))
  while True:
   try:
      choice = int(input('What is your choice:'))
      if choice >= 6 or choice <= 0:
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again')

  if userInput == 1:
    if choice in bestBuyList.keys():
      customerList.append((bestBuyList[choice][0], bestBuyList[choice][1]))
    else:
      print('Invalid Choice')

  elif userInput == 2:
    if choice in walmartList.keys():
      customerList.append((walmartList[choice][0], walmartList[choice][1]))
    else:
      print('Invalid Choice')

  elif userInput == 3:
    if choice in targetList.keys():
      customerList.append((targetList[choice][0], targetList[choice][1]))
    else:
      print('Invalid Choice')

  elif userInput == 4:
    if choice in costcoList.keys():
      customerList.append((costcoList[choice][0], costcoList[choice][1]))
    else:
      print('Invalid Choice')

  elif userInput == 5:
    if choice in ralphsList.keys():
      customerList.append((ralphsList[choice][0], ralphsList[choice][1]))
    else:
      print('Invalid Choice')
  while True:
   try:
    keepChoosing = input('\nWant to keep shopping? Y for yes, N for no: ').upper()
    if keepChoosing == 'Y' or keepChoosing == 'N':
      break
    else:
      raise AssertionError  
   except AssertionError:
      print('Invalid Input! Please enter a Y or N')
  
#import PersonClass  
salesModule.total(customerList)