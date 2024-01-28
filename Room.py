import logging
logging.basicConfig(filename = "Hotel management" , level = logging.INFO , format = "%(asctime)s / %(message)s")
class Room:
    def __init__(self , room_id , room_type  ,  capacity , room_status  ):
        self.room_id = room_id
        self.room_type = room_type 
        self.capacity = capacity
        self.room_status = room_status
        #self.maintenance = False
        #self.maintenance_requests = []
        self.booked = {}
        self.booked = False
        self.checked = {}
        self.checked = True
        self.repaired = True
        self.cleaned = True
        self.room_book = False

        logging.info(f"there is room with Id: {self.room_id} , Type: {self.room_type} , Capacity: {self.capacity} , Status: {self.room_status}")

   
    def __str__(self):
        return f"Id: {self.room_id} , Type: {self.room_type} , Capacity: {self.capacity} , Status: {self.room_status}"
    


    def set_room_status(self):
        
        self.new_status = input("new status : booked/checked/repaired/cleaned ?? ")
        print(f"new status is {self.new_status}")
        
    def schedule_room_maintenance(self , maintenance_type ):
          self.maintenance_type = maintenance_type
          if self.maintenance_type == "False":
            print("room maintenance isn't done")
            logging.info(f"room maintenance is not done")
          elif self.maintenance_type == "True":
                print("room maintenance is done")
                logging.info(f"room maintenance is done")
          else:
                print("not found")
                
if __name__ == "__main__":
    r1 = Room("rr1" , "1" , "tak" , "booked")
    print(r1)
    #r1.set_room_status()
    r1.schedule_room_maintenance("True")

