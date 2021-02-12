class Classroom:
  classroom_list = ["Maths","Physics","Chemistry"]

  @staticmethod
  def search_classroom(classroom):
    if classroom in  Classroom.classroom_list:
      return "Found"
    else:
      return -1

print(Classroom.search_classroom("Physics"))


class Ticket:
  counter = 0

  def __init__(self,passenger_name,source,destination):
    self.passenger_name = passenger_name
    self.ticket_id = None
    self.source = source
    self.destination = destination

  def validate_source_destination(self):
    destination_list = ["Mumbai","Chennai","Pune","Kolkata"]
    if self.source == "Delhi" and self.destination in destination_list:
      return True
    else:
      return False
      
  def generate_ticket(self):
    if self.validate_source_destination():
      Ticket.counter+=1
      if Ticket.counter <= 9:
        self.ticket_id = self.source[0]+self.destination[0]+"0"+str(Ticket.counter)
      else:
        self.ticket_id = self.source[0]+self.destination[0]+str(Ticket.counter)
    else:
      self.ticket_id = None

  def get_ticket_id(self):
    return self.ticket_id

  def get_passenger_name(self):
    return self.passenger_name

  def get_source(self):
    return self.source

  def get_destination(self):
    return self.destination

t1 = Ticket("Abhinay","Delhi","Mumbai")

t1.generate_ticket()

print(t1.get_ticket_id())

