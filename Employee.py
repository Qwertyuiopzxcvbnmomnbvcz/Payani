from Student1 import *
class Employee(Person):
    def __init__(self , first_name , last_name , age , employee_code , salary ):
        super().__init__(first_name , last_name , age )
        self.employee_code = employee_code
        self.salary = salary
    def __str__(self):
        data = super().__str__()
        return f"{data} ,Emp_code: {self.employee_code} Salary: {self.salary}"
    def info_display(self):
        print(f"First_name: {self.first_name} , Last_name: {self.last_name} , Age: {self.age}")


if __name__ == "__main__":
    em1 = Employee("sara" , "sadeghi" , 54 , "321" , 11)
    print(em1)
    em1.info_display()
