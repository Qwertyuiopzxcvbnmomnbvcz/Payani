from Person import *
from Room import *
#logging.basicConfig(filename = "Hotel management" , level = logging.INFO , format = "%(asctime)s / %(message)s")

class Guests(Person):
    
    def __init__(self , id_ , name , last_name , age , contact_info , number):
        super().__init__( id_ , name , last_name , age , contact_info)
        
        self.guest_id = id_
        self.number = number
        self.book = {
            "1nafare" : 145,
            "3nafare" : 541}
        logging.info(f"this is guest with Id: {self.guest_id} , Name: {self.name} , Last_name: {self.last_name} ,Number: {self.number} ")
        
    def __str__(self):
        return f"{super().__str__()} , Number: {self.number}"

    def dis_role(self):
        print(f"{self.name} is a guest .")
    
    def request_room_booking(self , start_date , end_date ):
        self.start_date = start_date
        self.end_date = end_date
        self.bookings = {}
        room_type = input("2nafare/5nafare :")
        if room_type == "2nafare":
            self.bookings["room_2nafare"] = "2takhte"
            print(f"{self.bookings} booked from:  {self.start_date} to {self.end_date} ")
        elif room_type == "5nafare":
            self.bookings["room_5nafare"] = "5takhte"
            print(f"{self.bookings} booked from:  {self.start_date} to {self.end_date} ")
        else:
            print("not exist")
            logging.info(f"{self.bookings} room are booked  from:  {self.start_date} to {self.end_date} ")
         
    def amend_booking(self , booking_id , new_start_date , new_end_date ):
        self.booking_id = booking_id
        self.new_start_date = new_start_date
        self.new_end_date = new_end_date
        for v in self.book.values():
            if booking_id != v:
                print(f"this room with Id: {self.booking_id} amended date from: {self.new_start_date} to {self.new_end_date}")

            else:
                print("room not amend")
            break
        

    def cancel_booking(self , booking_id):
        
         self.booking_id = booking_id
         for v in self.book.values():
             if booking_id == v:
                  del self.book
                  print(f"this room with Id: {self.booking_id} canceled ")
                  logging.info(f"room: {self.booking_id} canceld")
             else:
                 print(f"this room with Id: {self.booking_id} not canceled ")
             break

    def give_feedback(self):

        self.feedback = input("request_room_booking/amend_booking/cancel_booking :  ")
        if self.feedback == "request_room_booking":
             request = Guests.request_room_booking(self , start_date = 1 , end_date = 2 )
             logging.info("request_room_booking has feedback: {request}")
        elif self.feedback == "amend_booking":
             amend = Guests.amend_booking(self , booking_id = "123" , new_start_date = 3 , new_end_date = 4 )
             logging.info("amend_bookin has feedback: {amend}")
        elif self.feedback == "cancel_booking":
             cancel = Guests.cancel_booking(self , book_id = "123" , booking_id = "123")
             logging.info("cancel_booking hasa feedback: {cancel}")
        else:
             print(f"command not found ")
            
if __name__ == "__main__":
    g1 = Guests("123" ,"g1" , "g" , 30 , 8754 , 6)
    #print(g1)
    #g1.request_room_booking(7 , 8)
    #g1.amend_booking("123" ,9,10)
    #g1.cancel_booking("145")
    #g1.give_feedback()
