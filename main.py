class Customer:
  def __init__(self,cust_id,cust_name,age,wallet_balance):
    self.cust_id = cust_id
    self.cust_name = cust_name
    self.age = age
    self.__wallet_balance = wallet_balance

  def update_balance(self,amount):
    if amount > 0 and amount < 1000:
      self.__wallet_balance += amount

  def show_balance(self):
    print("Available Balance : ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
# c1.update_balance(500)
c1._Customer__wallet_balance = 10000000000
c1.show_balance()

# print(c1.__wallet_balance)


