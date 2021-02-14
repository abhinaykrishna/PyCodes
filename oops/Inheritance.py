# 1. An apparel shop wants to manage the items which it sells.


class Apparel:
  counter = 100
  def __init__(self,price,item_type):
    
    self.price = price
    self.item_type = item_type
    # self.item_id = None

    Apparel.counter+=1

    if self.get_item_type().lower() == "cotton" or self.get_item_type().lower() == "silk":
      self.item_id = self.get_item_type()[0]+str(Apparel.counter)
    
  def get_item_type(self):
    return self.item_type

  def get_item_id(self):
    return self.item_id

  def get_price(self):
    return self.price

  def set_price(self,price):
    self.price = price

  def calculate_price(self):
    self.price = 1.05 * self.price
    # return self.__price

class Cotton(Apparel):

  def __init__(self,price,discount):
    super().__init__(price,"Cotton")
    self.discount = discount

  def calculate_price(self):
    # temp_price = super().calculate_price()
    # temp_price = temp_price *  temp_price - (self.__discount/100)
    # temp_price = 1.05 * temp_price
    # self.__price = temp_price
    # print("Total Cotton Price ",self.__price)
    super().calculate_price()
    self.price = self.price - self.price * self.discount/100
    self.price += self.price * 5/100

  def get_discount(self):
    return self.discount

class Silk(Apparel):
  def __init__(self,price):
    super().__init__(price,"Silk")
    self.__points = 0 

  def calculate_price(self):
    # self.__price = super().calculate_price()
    super().calculate_price()
    if self.price > 10000:
      self.__points += 10
    else:
      self.__points += 3

    # t = self.get_price() * 1.10
    # self.set_price(t)

    self.price += self.price*10/100

  def get_points(self):
    return self.points

c1 = Cotton(10000,10)
s1= Silk(20000)

print(c1.price)
c1.calculate_price()
print(c1.price)
print(s1.price)
s1.calculate_price()
print(s1.price,s1.get_points())



# 2. Spice Hut is a tiffin service provider which home delivers dinner to their customers – Occasional customers and Regular customers.

class Customer:
  
  def __init__(self,customer_name):
    self.__customer_name = customer_name
    self.bill_amount = None
    self.bill_id = None

  # @abstractmethod
  def calculate_bill_amount(self):
    pass

  def get_customer_name(self):
    return self.__customer_name

class OccasionalCustomer(Customer):
  counter = 1000
  def __init__(self,customer_name,distance_in_kms):
    super().__init__(customer_name)
    self.__distance_in_kms = distance_in_kms
    OccasionalCustomer.counter += 1
    self.bill_id = "O"+str(OccasionalCustomer.counter)

  def get_distance_in_kms(self):
    return self.__distance_in_kms

  def validate_distance_in_kms(self):
    if self.get_distance_in_kms() >=1 and self.get_distance_in_kms() <= 5:
      return True
    else:
      return False

  def calculate_bill_amount(self):
    if self.validate_distance_in_kms():
      if self.get_distance_in_kms() <=2:
        self.bill_amount = 50 + 5 * self.get_distance_in_kms()
      else:
        self.bill_amount = 50 + 7.5 * (self.get_distance_in_kms()-2)
      
    else:
      self.bill_amount = -1
    
    return self.bill_amount

class RegularCustomer(Customer):
  counter = 1000
  def __init__(self,customer_name,no_of_tiffin):
    super().__init__(customer_name)
    self.__no_of_tiffin = no_of_tiffin
    RegularCustomer.counter+=1
    self.bill_id = "R"+str(RegularCustomer.counter)

  def validate_no_of_tiffins(self):
    if self.get_no_of_tiffins() >= 1 and self.get_no_of_tiffins() <= 5:
      return True
    else:
      return False

  def get_no_of_tiffins(self):
    return self.__no_of_tiffin

  def calculate_bill_amount(self):
    if self.validate_no_of_tiffins():
      self.bill_amount = 50 * self.get_no_of_tiffins()
    else:
      self.bill_amount = -1
    
    return self.bill_amount

c1 = OccasionalCustomer("Mike",4)
c2 = RegularCustomer("John",2)
c3 = OccasionalCustomer("Lisa",8)
c4 = RegularCustomer("Andy",5)

print(c1.calculate_bill_amount())
print(c2.calculate_bill_amount())
print(c3.calculate_bill_amount())
print(c4.calculate_bill_amount())