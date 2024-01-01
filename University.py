from Student1 import*
from Employee import *
class University():
    def __init__(self,name):
        self.name = name
        self.students = []
        self.employees = []
        
    def add_student(self , obj):
        if obj.student_code not in self.students:
            self.students.append(obj.student_code)
            print("Added!")
        else:
            print("not found!")
    def add_employee(self , obj):
        if obj.employee_code not in self.employees:
            self.employees.append(obj.employee_code)
            print("Added!")
        else:
            print("not found!")


    def remove_student(self , obj):
        if obj.student_code in self.students:
            self.students.remove(obj.student_code)
            print("Removed!")
        else:
            print("not found!")

    def remove_employee(self , obj):
        if obj.employee_code in self.employees:
            self.employees.remove(obj.employee_code)
            print("Removed!")
        else:
            print("not found!")


    def search_student(self , student_code):
        for dict_ in self.students:
            for i in dict_:
                if i.student_code == student_code:
                    print(i)
                    
    def edit_student(self,student_code ,first_name = None , last_name = None):
        student_code = input("stu code :  ")
        if student_code in self.students:
            self.first_name = first_name or self.first_name
        else:
            print("not found")
    def edit_employee(self,employee_code ,first_name = None , last_name = None):
        employee_code = input("emp code :  ")
        if employee_code in self.employees:
            self.first_name = first_name or self.first_name
        else:
            print("not found")

            
            
        
if __name__ == "__main__":
    u1 = University("u1")
    st1 = Student("zahra" , "Shaabani" , 20 , "123" , 18)
    em1 = Employee("sara" , "sadeghi" , 54 , "321" , 11)
    u1.add_student(st1)
    print(vars(u1))
    u1.add_employee(em1)
    print(vars(u1))
    #u1.remove_student(st1)
    #print(vars(u1))
    #u1.remove_employee(em1)
    #print(vars(u1))
    #u1.search_student("123")
    #print(vars(u1))
    #u1.edit_student("123" ,first_name = "fati")
    #print(vars(u1))
    u1.edit_employee("321" ,first_name = "shiva")
    print(vars(u1))

    
