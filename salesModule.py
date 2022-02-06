f = open('receipt.txt','w')

tax = 0.0775
def total(customerList):

  subtotal = 0
  for i in customerList:
    subtotal +=(i[1])

  print(customerList)
  print('Subtotal: $ {:.2f}'.format(subtotal))

  shipping = subtotal * 0.05
  print('Shipping: $ {:.2f}'.format(shipping))

  totalAmount = tax*subtotal
  print('Tax: \t $ {:.2f}'.format(totalAmount))

  total = subtotal + totalAmount + shipping
  print('Total: \t $ {:.2f}'.format(total))

  receipt(customerList, subtotal, total, shipping,totalAmount)

def printList(storeList,storeNum):
  print('\nYou chose {}'.format(storeNum) + '. These are their available products.')
  print('')
  for k, v in storeList.items():
    print('{}) {}: $ {}'.format(k, v[0], v[1]))
  print('(Shipping costs will be 5% of your subtotal.)')
    

def receipt(customerList, subtotal, total, shipping,totalAmount):

  f.write('****RECEIPT****\n')
  f.write('Item       Price\n')
  f.write('----       ----\n')

  for i in customerList:
    f.write('{} $ {} \n'.format(i[0],i[1]))

  f.write('''
----------------------
Subtotal:   ${:.2f}
Shipping:   ${:.2f}
Tax:        ${:.2f}
Total:      ${:.2f}
---------------------
Thank you for shopping with us...
'''.format(subtotal, shipping, totalAmount,total))

  f.close()
  print('\nYour receipt has been printed in the receipt.txt file')