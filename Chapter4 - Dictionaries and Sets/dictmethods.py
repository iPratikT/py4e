info = {
    "key1": "value1",
    "name": "Pratik", 
    "age": 30, 
    "city": "Munich",
    "is married": True,
    "marks": "[90, 80, 70]",
    "hobbies": ("reading", "traveling", "coding")
}

print(info.keys()) # returns all keys
print(list(info.keys())) # returns all keys as list
print(len(info.keys())) # returns the total number of keys
print(info.values()) # returns all values 
print(info.items()) # returns all key value pairs as tuple

pairs = list(info.items())
print(pairs[2]) # returns the item as tuple at the requested key

#get method
print("using the get method to get value of key instead of directly passing key name")
print(info["name"]) # will return error if key "name" does not exist
print(info.get("name")) # will return None if key "name" does not exist -> helps in running the remaining code error free

#update method
info.update({"phone" : +496541684})
#print(info.items())

#method2
new_dict={"hasACar":False}
info.update(new_dict)
print(info.items())