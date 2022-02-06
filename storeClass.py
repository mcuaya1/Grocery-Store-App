class Store:
  def __init__(self):
    self.storeName
    self.storeList

  def showStore(self):
    print(self.storeName)

  def showStoreItems(self):
    for k, v in self.storeList.items():
      print('{}) {}: $ {}'.format(k, v[0], v[1]))
      print('(Shipping costs will be 5% of your subtotal.)') 


class BestBuy(Store):
  def __init__(self):
    super(). __init__()
    self.storeName = 'Best Buy'
    self.storeList = {1:('Laptop',299.99), 2:('Gaming PC',1029.99),3:('TV',249.99),4:('Xbox One',219.99),5:('Nintendo Switch', 279.99)}
    

class Walmart(Store):
  def __init__(self):
    self.storeName = 'Walmart'
    self.storeList = {1:('Apple',2.99), 2:('Pie',9.99),3:('Juice',10.99),4:('Xbox One',219.99),5:('Nintendo Switch', 279.99)}

bestBuy = BestBuy()
walmart = Walmart()

