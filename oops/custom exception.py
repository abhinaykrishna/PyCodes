class Mechanic:
  def __init__(self,mechanic_id,specialization,vehicle_count):
    self.__mechanic_id = mechanic_id
    self.__specialization = specialization
    self.__vehicle_count = vehicle_count

  def get_mechanic_id(self):
    return self.__mechanic_id
  
  def get_specialization(self):
    return self.__specialization

  def get_vehicle_count(self):
    return self.__vehicle_count

  def set_mechanic_id(self,mechanic_id):
    self.__mechanic_id = mechanic_id

  def set_specialization(self,specialization):
    self.__specialization = specialization

  def set_vehicle_count(self,vehicle_count):
    self.__vehicle_count = vehicle_count

class VehicleService:
  def __init__(self,mechanic_list):
    self.mechanic_list = mechanic_list

  def assign_vehicle_for_service(self,mechanic_id,vehilce_list):

    vehicle_assigned_to_id = dict()

    if mechanic_id in self.mechanic_list:
      for vehicle in vehilce_list:
        if mechanic_id.get_specialization() == vehicle:
          vehicle_assigned_to_id[mechanic_id] = vehicle
          mechanic_id.vehicle_count+=1
          print("Total Vehicles Assigned to Mechanic: "+str(mechanic_id.get_mechanic_id()+" are "+str(mechanic_id.get_vehicle_count)))
        else:
          raise InvalidMechanicSpecializtionException()
    else:
      raise InvalidMechanicIDException()

class InvalidMechanicIDException(Exception):
  def __init__(self):
    super().__init__("Invalid Mechanic ID")

class InvalidMechanicSpecializtionException(Exception):
  def __init__(self):
    super().__init__("Invalid Mechanic Specialization")

try:
  m1 = Mechanic(101,"TW",1)
  m2 = Mechanic(102,"FW",0)
  m3 = Mechanic(103,"TW",4)
  m4 = Mechanic(104,"FW",2)
  m5 = Mechanic(105,"FW",1)

  v1 = VehicleService([m1,m2,m3,m4,m5])
  v1.assign_vehicle_for_service(m1,["FW","TW"])

  # v2 = VehicleService([m1,m2,m3,m4,m5])
  # v2.assign_vehicle_for_service(m6,["FW","TW"])

except InvalidMechanicIDException as e:
  print(str(e))
except InvalidMechanicSpecializtionException as e:
  print(str(e))
except Exception as e:
  print("Something Went Wrong "+str(e))
