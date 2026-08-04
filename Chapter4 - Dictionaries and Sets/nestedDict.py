# dictionary defined within dictionary

student = {
    "name": "Pratik", 
    "age": 30, 
    "city": "Munich",
    "is married": True,
    "subjects" : {
        "physics": 30,
        "chemistry": 50,
        "math" : 90
    },
    "marks": "[90, 80, 70]",
    "hobbies": ("reading", "traveling", "coding")
}

print(type(student))
print(student["subjects"]["physics"])