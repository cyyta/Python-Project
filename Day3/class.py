# syntax
#class className:

class Student:
    age = 18   #static variable/attributes
    #for first student
   # std_name = "sita"
    #std_name = "nayan"  for second student
    def __init__(self,name,level,address):  #constructor
        print("constructor called")
        self.std_name = name
        self.std_level = level  #instatnce attributes 
        self.std_address = address

    def displyStudentName(self):
        print(self.std_name)

    def displyStudentDetails(self):
        print(self.std_level) 
        print(self.std_address)   


       #pass
    def add(): #static variable
        print("sum of 1 & 2" , 1+2)   
    

#@abs library
first_student = Student("sita","BCA","Birtamode")
second_student = Student("nayan","Bca","btm")
print(first_student.displyStudentName())
print(second_student.displyStudentDetails())
Student.add()
