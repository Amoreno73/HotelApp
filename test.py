class Room:
  
  def __init__(self,occupied, room_num, room_type, clean):
    # attributes
    self.occupied = occupied
    self.number = room_num
    self.room_type = room_type
    self.clean = clean
    
  # functions
  def cleanStatus(self):
    print(f"This room {self.clean} clean.")
        #  self.clean = "is" or "is not"
  def roomNumber(self):
    print(f"This is the room number: {self.number}.")
        # self.number = "245"
  def occupiedStatus(self):
    print(f"This room {self.occupied} occupied.")
        #  self.occupied = "is" or "is not"




test = Room("is", 125 , "S", "is")
test.cleanStatus()


