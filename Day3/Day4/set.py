#set unordered collection of unique element
#not repeat element

#first_set = {"aa",1,1,2,2,4,5,7,7,"sita"}
#print(first_set)


class Animal:

 def __init__(self,name):
    self.name = name 

 def displyMethod(self):
    print(self.name)
class Dog(Animal):  #dog inherit animal    
 def __init__(self,name): 
    super().__init__(name)
    super().displyMethod()
 def speak(self):
    print(f"{self.name} barks") 

dog_one = Dog("Dog 1")
dog_2 = Dog("Dog  2")
dog_one.displyMethod()
dog_2.speak()     


