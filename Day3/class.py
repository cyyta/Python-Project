# syntax
#class className:

class Student:
    age = 18   #static variable
    #for first student
   # std_name = "sita"
    #std_name = "nayan"  for second student
    def __init__(self,name,level,address):  #constructor
        print("constructor called")
        self.std_name = name
        self.std_level = level
        self.std_address = address
       #pass
    def add(): #static variable
        print("sum of 1 & 2" , 1+2)   
    

first_student = Student("sita","BCA","Birtamode")
second_student = Student("nayan","Bca","btm")
print(first_student.std_name)
print(second_student.std_name)
Student.add()
