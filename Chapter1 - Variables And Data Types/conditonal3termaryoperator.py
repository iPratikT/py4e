"""
in this 2 line program, we use the ternary if statement
along with logical operator

"""

food=input("Enter your food: ")
print ("sweet" if food=="cake" or food=="jalebi" else "not sweet")

# one more way is as follows:
age = int(input("Enter your age: "))
vote = ("yes", "no")[age >= 18]
# we didnt even use if keyword here, we just used logical operator and ternary operator


# one can also use clever if by using []
age = int(input("Enter your age: "))
vote=["You are not eligible to vote.", "You are eligible to vote."][age >= 18]
print(vote)

#another way of using clever if is by using dictionary
age = int(input("Enter your age: "))
vote={True: "You are eligible to vote.", False: "You are not eligible to vote."}[age >= 18]
print(vote)
