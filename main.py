class Customer:
  def __init__(self,name,age,phone_no,address):
    self.name = name
    self.age = age
    self.phone_no = phone_no
    self.address = address 

  def view_details(self):
    print(self.name,self.age,self.phone_no)
    print(self.address.get_door_no(),self.address.get_street(),self.address.get_pincode())

  def update_details(self,add):
    self.address = add

class Address:
  def __init__(self,door_no,street,pincode):
    self.__door_no = door_no
    self.__street = street
    self.__pincode = pincode
  
  def update_address(self):
    pass

  def get_door_no(self):
    return self.__door_no
  def get_street(self):
    return self.__street
  def get_pincode(self):
    return self.__pincode
  def set_door_no(self, value):
    self.__door_no = value
  def set_street(self, value):
    self.__street = value
  def set_pincode(self, value):
    self.__pincode = value

add1=Address(123, "5th Lane", 56001)
add2=Address(567, "6th Lane", 82006)

cus1=Customer("Jack", 24, 1234, add1)

cus1.view_details()

cus1.update_details(add2)

cus1.view_details()
