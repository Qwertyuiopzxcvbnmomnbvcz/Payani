from Admin import *
from Staff import *
from Guest import *
from Room import *
import logging
import json
class Hotel:
    def __init__(self , hotel_id , name , address ):
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.objects = {
			"staffs": {},
			"admins": {},
			"guests": {}
		}
        logging.info(f"Hotel with Id: {self.hotel_id} , Name: {self.name} is in  Address: {self.address}")
    def __str__(self):
        return f"Id: {self.hotel_id} , Name: {self.name} , Address: {self.address}"
    
    def list_available_rooms(self , room ):
        room.room_book = False
        self.rooms = ["a" , "b"]
        for i in self.rooms:
            print(i)

    def get_guest_details(self , obj):
            print(f"Guest with Name: {obj.name} , Age: {obj.age}")
            logging.info(f"Guest with Name: {obj.name} ,Last_name: {obj.last_name} , Age: {obj.age} , contact_info: {obj.contact_info}")

    def summarize_daily_operations(self):
        """res = type(obj).__name__
        res = res.lower()+"s"
        self.objects[res][obj.id_] = obj"""
        
        """for dict_ in self.objects.values():
              for i in dict_.values():
                    if i.name == name:
                        print(i)"""
        
        self.id_room = input("Please Enter your room id :  ")
        self.add = {}
        self.add["rooms"] = self.id_room
        print(self.add)
        print("room added")

if __name__ == "__main__":
    h1 = Hotel("h1" , "h" , "hh")
    g1 = Guests("123","g1" , "g" , 30 , 8754 , 6)
    r1 = Room("rr1" , "1" , "tak" , "booked")
    #print(h1)
    #h1.list_available_rooms(r1)
    #h1.get_guest_details(g1)
    #h1.summarize_daily_operations()
    

