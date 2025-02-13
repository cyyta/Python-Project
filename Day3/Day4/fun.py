#Function--is a reuseable block os code that perform specific task
#dry principle avoid repetition dont repeat code
#make debugging easier
#fun declaration def keyword
# to call fun

#def take_input():
    #print(f"sum of number is {1+3}")
    #task code of block
#can call function
#take_input()

#def sum(v1,v2=3): #parameters v1 and v2
    #default value is replaced by original value
    #print(v1+v2)
#sum(v1=20) #expect value 2 override
#sum(10,5)  
  # arguments 2,3

#return

def sum(a,b):
    #a=5 b=6
    c = a+b
    print("inside function") #return c

    return "function works propely"
sum(1,4)
result = sum(5,6) #result = 11
print(f"result is : {result}")
