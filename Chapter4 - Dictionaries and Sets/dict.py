info = {
    "key1": "value1",
    "name": "Pratik", 
    "age": 30, 
    "city": "Munich",
    "is married": True,
    "marks": "[90, 80, 70]",
    "hobbies": ("reading", "traveling", "coding")
}

# anything can be a key in dictionary but it should be immutable -> not list, set, dict.
# hence, tuple can be a key in dictionary 

print(info)
print(type(info))

# Accessing values from dictionary
print(info["name"])
print(info["age"])
