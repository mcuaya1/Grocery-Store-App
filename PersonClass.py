class Person:
  print('\n*****  WELCOME TO DELIVERY APP  *****\n')
  print('\nPlease register to be able to order\n')
  def __init__(self):
    self.name = None

  def showName(self):
    print(self.name)
  
class Customer(Person):
  def __init__(self):
    super().__init__()
    self.city = None
    self.address = None
    self.zip = None


customer1 = Customer()
 #isalpha
while True:
   try:
      customer1.name = input('Create a username: ')
      if customer1.name.isalnum() == False or customer1.name.isdigit() == True:
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again. Please enter only letters and numbers')

 #isalnum
while True:
   try:
      customer1.address = input('What is your address: ')
      if customer1.address.isalnum() == False and customer1.address.isspace() == True:
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again')


while True:
   try:
      customer1.city = input('What is your city: ')
      if customer1.city.isalpha() == False or customer1.name.isdigit() == True :
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again')

while True:
   try:
      customer1.personZip = input('What is your ZIP code: ')
      if len(customer1.personZip) <= 4 or customer1.personZip.isdigit() == False:
        raise ValueError
      else:
        break
   except ValueError:
      print('Invalid! Please try again')


print('\nHello : {}\nWe will deliver your order to this address {}, {} {}'.format(customer1.name, customer1.address, customer1.city, customer1.personZip))
print('\n')

