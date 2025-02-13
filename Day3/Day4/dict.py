#dictionary we cannot use same key as double
student = {
    "name": "shitoshna",
    "address": "birtamode"
   #0: "it is zero"
    
}
#print("Before change", student["name"])
#student["name"]="it is not zero"
#print("After change", student["name"])
for i in student:
    print(i["name"])
del student["name"]
