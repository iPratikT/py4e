# here we learn if, else, elif statements in python, while interacting with the user

age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are a minor.")