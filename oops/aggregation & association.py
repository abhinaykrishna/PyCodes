# Freight Pvt. Ltd, a cargo company, forwards cargos/freights between its customers.
# Freight charges are applied based on weight and distance of the shipment.
# Write a python program to implement the class diagram given below.

class Customer:
  def __init__(self,customer_id,customer_name,adderss):
    self.customer_id = customer_id
    self.customer_name = customer_name
    self.address = adderss

  def validate_customer_id(self):
    if len(str(self.customer_id)) == 6 and str(self.customer_id)[0] == "1":
      return True
    else:
      return False

  def get_customer_id(self):
    return self.customer_id

  def get_customer_name(self):
    return self.customer_name

  def get_address(self):
    return self.address

class Freight:
  counter = 198

  def __init__(self,recipient_customer,from_customer,weight,distance):
    self.recipient_customer = recipient_customer
    self.from_customer = from_customer
    self.weight = weight
    self.distance = distance
    self.freight_id = None
    self.freight_charge = None

  def validate_weight(self):
    if self.weight % 5 == 0:
      return True
    else:
      return False

  def validate_distance(self):
    if self.distance in range(500,5001):
      return True
    else:
      return False
  
  def forward_cargo(self):
    if self.from_customer.validate_customer_id() and  self.recipient_customer.validate_customer_id() and self.validate_weight() and self.validate_distance():
      Freight.counter + 2
      self.freight_id = Freight.counter
      self.freight_charge = 150*self.weight + 60*self.distance
    else:
      self.freight_charge = 0

  def get_freight_charge(self):
    return self.freight_charge

  def get_freight_id(self):
    return self.freight_id

  def get_recipient_customer(self):
    return self.recipient_customer

  def get_from_customer(self):
    return self.from_customer

  def get_weight(self):
    return self.weight

  def get_distance(self):
    return self.distance

c1 = Customer(123456,"Abhinay","d1")
c2 = Customer(198979,"Abhinay","d2")
c3 = Customer(787261,"Abhinay","d3")

f1 = Freight(c1,c2,5,1000)
f2 = Freight(c2,c1,10,2000)

f1.forward_cargo()
f2.forward_cargo()

print(f1.get_freight_charge())
print(f2.get_freight_charge())


# Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.
# They want to keep track of customers who buy fruits from them and also the billing process.
# Write a python program to implement the class diagram given below.

class FruitInfo:
  fruit_name_list = ["Apple","Guava","Orange","Grape","Sweet Lime"]
  fruit_price_list = [200,80,70,100,60]

  @staticmethod
  def get_fruit_price(fruit_name):
    for fruit in range(len(FruitInfo.fruit_name_list)):
      if FruitInfo.fruit_name_list[fruit] == fruit_name:
        return FruitInfo.fruit_price_list[fruit]
    else:
      return -1

  @staticmethod
  def get_fruit_name_list():
    return FruitInfo.fruit_name_list
  
  @staticmethod
  def get_fruit_price_list():
    return FruitInfo.fruit_price_list

# print(FruitInfo.get_fruit_price("Sweet Lime"))

# print(len(FruitInfo.fruit_name_list))

# print(FruitInfo.get_fruit_name_list())

# print(FruitInfo.get_fruit_price_list())

class Purchase:
  counter = 101

  def __init__(self,customer,fruit_name,quantity):
    self.customer = customer
    self.fruit_name = fruit_name
    self.quantity = quantity
    self.purchase_id = None

  def get_purchase_id(self):
    return self.purchase_id

  def get_customer(self):
    return self.customer

  def get_quantity(self):
    return self.quantity

  def calculate_price(self):
    if FruitInfo.get_fruit_price(self.fruit_name) != -1:

      if ( max(FruitInfo.get_fruit_price_list()) == FruitInfo.get_fruit_price(self.fruit_name) ) and self.quantity > 1:
        price = 0.98 * self.quantity * max(FruitInfo.get_fruit_price_list())
      elif ( min(FruitInfo.get_fruit_price_list()) == FruitInfo.get_fruit_price(self.fruit_name) ) and self.quantity > 5:
        price = 0.95 * self.quantity * min(FruitInfo.get_fruit_price_list())
      else:
        price = self.quantity * FruitInfo.get_fruit_price(self.fruit_name)

      Purchase.counter += 1
      self.purchase_id = "P"+str(Purchase.counter)

      if self.customer.customer_type == "wholesale":
        print("As you are a WHOLESALE customer we have added 10% extra discount")
        price = 0.90 * price
        return price
      else:
        return price
      
    else:
      return -1



class Customer:
  def __init__(self,customer_name,customer_type):
    self.customer_name = customer_name
    self.customer_type = customer_type

  def get_customer_name(self):
    return self.customer_name

  def get_customer_type(self):
    return self.customer_type

c1 = Customer("Krishna","wholesale")
c2 = Customer("Margaret","occasional")

p1 = Purchase(c1,"Sweet Lime",7)
p2 = Purchase(c2,"Apple",3)

print(p1.calculate_price())
print(p1.get_purchase_id())

print(p2.calculate_price())
print(p2.get_purchase_id())

# Care hospital management wants to calculate the charge of lab tests done by its patients.
# Write a python program to implement the class diagram given below.

class Patient:

  def __init__(self,patient_id,patient_name,list_of_lab_test_ids):
    self.patient_id = patient_id
    self.patient_name = patient_name
    self.list_of_lab_test_ids = list_of_lab_test_ids
    self.lab_test_charge = 0

  def get_patient_id(self):
    return self.patient_id
  
  def get_patient_name(self):
    return self.patient_name

  def get_list_of_lab_test_ids(self):
    return self.list_of_lab_test_ids

  def get_lab_test_charge(self):
    return self.lab_test_charge

  def calculate_lab_test_charge(self):
    for tests_performed in self.list_of_lab_test_ids:
      if LabTestRepository.get_test_charge(tests_performed) != -1:
        self.lab_test_charge += LabTestRepository.get_test_charge(tests_performed)
      else:
        self.lab_test_charge += 0


class LabTestRepository:
  list_of_hospital_lab_test_ids = [101,102,103,104,105]
  list_of_lab_test_charge = [1000,2000,3000,4000,5000]

  @staticmethod
  def get_test_charge(lab_test_id):
    for test_id in range(len(LabTestRepository.list_of_hospital_lab_test_ids)):
      if lab_test_id == LabTestRepository.list_of_hospital_lab_test_ids[test_id]:
        return LabTestRepository.list_of_lab_test_charge[test_id]
    else:
      return -1

# print(LabTestRepository.get_test_charge(104))

p1 = Patient("P123","John",[103,105,104,100])
p1.calculate_lab_test_charge()
print(p1.get_lab_test_charge())
