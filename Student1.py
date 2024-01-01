from Person import *
class Student(Person):
    def __init__(self , first_name , last_name , age , student_code , score ):
        super().__init__(first_name , last_name , age)
        self.student_code = student_code
        self.score = score
    def __str__(self):
        data = super().__str__()
        return f"{data} , Stu_code: {self.student_code} Score: {self.score}"
    def info_display(self):
        print(f"First_name: {self.first_name} , Last_name: {self.last_name} , Age: {self.age}")

if __name__ == "__main__":
    st1 = Student("zahra" , "Shaabani" , 20 , "123" , 18)
    print(st1)
    st1.info_display()
