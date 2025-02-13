class Student:
    school_name = "mmc"

    #id #name

    def __init__(self,id,name):
        #pass
        self.id = id    #instance varible
        self.name = name
        #instance method
    def displyStudentDetails(self):
        print(self.id)
        print(self.name)  
student_one = Student(100,"sita")
student_one.displyStudentDetails() 
#Student.displyStudentDetails()  if in case of static variable we use class to call method     