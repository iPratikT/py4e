"""This is a simple program that takes user input for name and age, 
and then prints a greeting message.
"""


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print ("Hello, " + name + "! You are " + age + " years old.")


"""
this is a typical error that we might usually miss:
name = input("Enter your name: ")
age = input("Enter your age: ")
here both name and age are strings, 
so we need to convert age to an integer using int() function.
"""