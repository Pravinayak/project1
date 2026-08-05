student={
    "name":"Pravi",
    "reg":42,
    "phno":9999
}
#printing the dictionary
print(student)

#changing the key"s value 
student["phno"]=777
print(student)

#adding  key & values to dict

student["dept"]="CSE"
print(student)

#adding more /multiple  key & values to dict

student["dept"]={"CSE","AIML","EEE"}
print(student)

#adding sub dictionaries to the existing dict
student['phno']={"Tel":123,"office":456,"home":7789}
print(student)

#Deleting the key value from the dict

del student["dept"]
print(student)