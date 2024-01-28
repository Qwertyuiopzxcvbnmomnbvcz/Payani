from Staff import *
from Person import *
from Room import *
import json
class Admin(Person):
     def __init__(self , id_ , name , last_name , age , contact_info , salary ):
        super().__init__(id_ ,name , last_name , age , contact_info )
        self.salary = salary
        self.role = "admin"
        logging.info(f"there is an admin with Id: {self.id_} , Name: {self.name} , Last_name: {self.last_name} , Contact_info: {self.contact_info} , Salary: {self.salary}")
        self.staffs = {}
        
     def __str__(self):
        return f"{super().__str__()} , Salary: {self.salary} , Role: {self.role}"
    
     def dis_role(self):
        print(f"{self.name} is an admin .")
    
     def create_staff_account(self , obj):
        if obj.id_ not in self.staffs:
            self.staffs[obj.id_] = obj
            print("created!")
            logging.info(f"created staff  with {self.name} {self.last_name}")
        else:
            print("exist")

     def remove_staff_member(self , obj):
        if obj.id_ in self.staffs:
            self.staffs.pop(obj.id_)
            print("Removed!")
            logging.info(f"removed staff  with {self.name} {self.last_name}")
        else:
            print("not found")


     def update_staff_role(self , obj , new_role = None):
        if obj.id_ in self.staffs:
            self.role = new_role or self.role
            self.staffs[obj.id_] = self.role
            print("Updated")
            logging.info(f"updated staff  with {self.name} {self.last_name}")
        else:
            print("not found")

     def approve_maintenance_request(self , room_id ):
        self.maintenance = True
        self.room_id = room_id
        if self.maintenance :
            print("check the maintenance_request") 
            logging.info(f"maintenance_request with Id: {self.room_id} approved")
        else:
            print("maintenance_request not check")
     
     def generate_payroll_report(self,obj):
         logging.info(f"generate_payroll with Salary: {obj.salaries}")
         self.payroll = input("True , False :  ")
         if self.payroll == "True":
             print(f"salaries: {obj.salaries}")
         elif self.payroll == "False":
             print("salary  not exist")

if __name__ == "__main__":
     #a1 = Admin("a123","a1","a",21,12345,3000)
     try:
          a1 = Admin("a123","a1","a",21,12345,3000)
     except TypeError as e:
          print(f"{e.__class__.__name__}: {e}")
     else:
          print(a1)
     finally:
          print("end")
         
     #print(a1) 
     s1 =  Staff("ss1","s1","s",35,1234)
     #a1.dis_role()
     #a1.create_staff_account(s1)
     #print(vars(s1))
     #a1.remove_staff_member(s1)
     #a1.update_staff_role(s1,"maintenance")
     #print(a1)
     #print(s1)
     r1 = Room("rr1" , "1" , "tak" , "a")
     #a1.approve_maintenance_request("rr1")
     #a1.generate_payroll_report(s1)


