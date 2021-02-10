# WeCare insurance company wants to calculate premium of vehicles.
# Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
# Premium amount is 2% of the vehicle cost for two wheeler and 6% of the vehicle cost for four wheeler. Calculate the premium amount and display the vehicle details.
# Write a Python program to implement the class chosen with its attributes and methods.
# Note:
# 1. Display appropriate error message, if the vehicle type is invalid
# 2. Perform case sensitive string comparison

class Vehicles:
  def __init__(self,vehicle_type,vehicle_id,vehicle_cost):
    self.vehicle_type = vehicle_type
    self.vehicle_id = vehicle_id
    self.vehicle_cost = vehicle_cost
    self.premium = 0
    self.flag = 0

  def calulate_premium(self):
    if self.vehicle_type == "Two Wheeler":
       self.premium = 0.02 * self.vehicle_cost
    elif self.vehicle_type == "Four Wheeler":
      self.premium = 0.06 * self.vehicle_cost
    else:
      self.flag = 1

  def display_vehicle(self):
    if self.flag == 0: 
      print( "Type : ",self.vehicle_type)
      print( "ID : ",self.vehicle_id)
      print( "Cost : ",self.vehicle_cost)
      print( "Premium : ",self.premium)
    else:
      print("Vehicle Type is Invalid - Must be either 2 or 4 Wheeler")

veh1 = Vehicles("Four Wheeler","83309",1000000)

veh1.calulate_premium()
veh1.display_vehicle()

print("-----------------------")

veh2 = Vehicles("Two Wheeler","93309",500000)
veh2.calulate_premium()
veh2.display_vehicle()

print("-----------------------")

veh3 = Vehicles("Three Wheeler","13245",200000)
veh3.calulate_premium()
veh3.display_vehicle()


# Consider the below scenario of a retail store.
# Implement the Customer class based on the identified class structure and details given below:
#     1. Consider all instance variables and methods to be public
#     2. Assume that bill_amount is initialized with total bill amount of the customer
#     3. Customer is eligible for 5% discount on the bill amount
#     4. purchases(): Compute discounted bill amount and pay bill
#     5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>
# Represent few customers, invoke purchases() method and display the details.


class Customer:
  def __init__(self,customer_name,bill_amount):
    self.customer_name = customer_name
    self.bill_amount = bill_amount

  def purchases(self):
    self.bill_amount = 0.95 * self.bill_amount
    Customer.pays_bill(self,self.bill_amount)

  def pays_bill(self,amount):
    print(self.customer_name ,"pays bill amount of Rs.",amount)

c1 = Customer("Abhinay",500)
c1.purchases()

c2 = Customer("Krishna",1200)
c2.purchases()

c3 = Customer("Gopal",1760)
c3.purchases()