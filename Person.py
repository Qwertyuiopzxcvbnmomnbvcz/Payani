from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self , first_name , last_name , age  ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"First_name: {self.first_name} , Last_name: {self.last_name} , Age: {self.age}"
    @abstractmethod
    def info_display(self):
        pass
if __name__ == "__main__":
    p1 = Person("a" , "b" , 30 , 21)
    print(p1)
