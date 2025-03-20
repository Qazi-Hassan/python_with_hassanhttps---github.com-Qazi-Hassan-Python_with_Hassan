## Dictionaries are used to store data values in Key:value pair
# unordered collection of elements
# mutable (changeable) 
#do not allow duplicate keys

#example of a Dictionary (including List & Tuples)
dict = { "name":"ali", "age": 23, "subjects": [ "python","maths", "statistics",
        "ML" ], "topics": ("data science", "AI"), "country": "pakistan", "height": 5.9, }
print(dict)  
# finding type
print(type(dict)) 

print(dict["name"])
print(dict["country"])

# reassigning any value
dict["name"] = "Hassan"
print(dict)
# nexted Dictionary e.g  Dict = { "key": "value" = "dic" }  or dictionary within a dictionary
students = { "name": "ali", "age":23, "subject": { "phy": 55, "chem": 60, "Bio":65 }, "weight": 70.5 }
print(students)
print(type(students))

## Dictionary Methods
# myDict.key()          returns all keys
print(dict.keys())
# myDict.values()        returns all values
print(dict.values())
# myDict.items()         returns all (key,val) pairs as tuples
print(dict.items()) 
# myDict.get()           returns the key accordig to value
print(dict["name"])
print(dict.get("name"))
#length of dictionary
print(len(dict))

