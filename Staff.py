from Person import *
from Room import *
from Guest import *

class Staff(Person):
    def __init__(self ,id_ , name , last_name , age , contact_info ):
        super().__init__(id_ ,name , last_name , age , contact_info )
        self.salaries = {
            "s_receptionist" : 900, 
            "s_housekeeping" : 800,
            "s_maintenance" :700
        }
        
        logging.info(f"there is an staff with Id: {self.id_} , Name: {self.name}, Last_name: {self.last_name} , Contact_info: {self.contact_info}  ,Salary: {self.salaries}")

    def __str__(self):
        return f"{super().__str__()} , Role: {self.role} , Salary: {self.salaries} "

    def dis_role(self):
        print(f"{self.name} is a staff .")

        
class Receptionist(Staff):
    def book_guest(self ,obj , room_id):
        self.room_id=room_id
        self.booked = {}
        if obj.room_id not in self.booked:
            self.booked["obj.room_id"] = obj
            print("room is booked")
            logging.info(f"Room: {obj.room_id} is booked ")
        else:
            print("not  found")
            logging.info(f"Room: {obj.room_id} is not  booked ")
              
    def check_out_guest(self ,obj, guest_id ):
        
        self.checked = {}
        self.guest_id = guest_id
        if obj.guest_id in self.checked:
            self.checked["obj.guest_id"] = obj
            print("room is checked")
            logging.info(f"Room by: {obj.guest_id} is checked ")
        else:
            print("not found ")
            logging.info(f"Room by: {obj.guest_id} is not checked ")

class Housekeeping(Staff):
    def add_room(self,room):
        self.rooms_ = {}
        if room.room_id not in self.rooms_:
            self.rooms_["room.room_id"]=room
            print("room_id added")
        else:
            print("not found")
            
    def mark_room_cleaned(self , obj  ):
        if obj.room_id not in self.rooms_ :
            obj.cleaned = True
            print("cleaned")
        else:
            print("not found")*
            
            
    def request_cleaning_supplies(self):
        
        self.suplies = {}
        self.sup = []
        for i in range (3)  :
            cleaning_s = input("Please enter 3 suplies :  ")
            self.sup.append(cleaning_s)
            self.suplies["cleaning_suplies"] = self.sup
            print(self.suplies)
            logging.info(f"there are some cleaning_splies {self.suplies}")        

class Maintenance(Staff):**
    
    def report_repair_done(self , room):
        room.repaired = True
        logging.info("Room: {self.room_id} repair reported done")
        print("reported.")
        
    def order_repair_materials(self): 
        self.materials = {}
        self.mat = []
        for m in range(3):
            materials = input("Please enter materials :  ")
            self.mat.append(materials)
            self.materials["repair_materials"] = self.mat
            print(self.materials)
            logging.info("There are repair_materials: {self.materials}")
    
    
    if __name__ == "__main__":
        s1 = Staff("ss1","s1","s",30,"1234")
        r1 = Room("r1" , "one" , 1 , "a")
        g1 = Guests("gg1" ,"g1" , "g" , 30 , 8754 , 6)
        rr1 = Receptionist("rr1","r1","r",25,"6543")
        hh1 = Housekeeping("hh1","h1","h",27,"8654")
        try:
            hh1.request_cleaning_supplies(self)
        except ValueError as e:
            print(e)
        except NameError as e:
            print(e)
        else:
            print(cleaning_s )
        finally:
            print("end")
            
        #mm1 = Maintenance("mm1","m1","m",32,"9876")
        #s1.dis_role()
        #rr1.book_guest(r1,"r1")
        #rr1.check_out_guest(g1,"gg1")
        #hh1.add_room(r1)
        #hh1.mark_room_cleaned(r1)
        hh1.request_cleaning_supplies()
        #mm1.report_repair_done(r1)
        #mm1.order_repair_materials()
        

   
