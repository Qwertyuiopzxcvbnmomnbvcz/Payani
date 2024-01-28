from abc import ABC,abstractmethod
import logging
from datetime import datetime
import json
logging.basicConfig(filename = "Hotel management" , level = logging.INFO , format = "%(asctime)s / %(message)s")
class Person(ABC):
    def __init__(self , id_ , name , last_name ,age , contact_info ):
        self.id_ = id_
        self.name = name
        self.last_name = last_name
        self.age = age
        self.contact_info = contact_info
        logging.info(f"there is a person with Id: {self.id_} , Name: {self.name} , Last_name: {self.last_name} , Contact_info: {self.contact_info}")

    def __str__(self):
        return (f"Id: {self.id_} ,"
                 f"Name: {self.name} ,"
                 f" Last_name: {self.last_name} ,"
                 f"Age: {self.age} ,"
                f" Contact_info: {self.contact_info}")
    
    def update_contact_details(self , new_contact_info = None):
        new_contact_info = input("Enter contact information:  ")
        self.coontact_info = new_contact_info or self.contact_info
    
    @abstractmethod
    def dis_role(self):
        pass

    


