class Athlete:
  def __init__(self, name, gender):
    self.__name = name
    self.__gender = gender

  def running(self):
    if (self.__gender == "girl"):
      print("150mtr running")
    else:
      print("200mtr running")

  def get_runner(self):
    return self.__name

  def set_gender(self,value):
    self.__gender = value

R1 = Athlete("Maria","Girl")
R1.set_gender("girl")
R1.get_runner()
R1.running()
