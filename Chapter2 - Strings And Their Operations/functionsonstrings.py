str = "i am a coder"

# to check if the string ends with "r"
print(str.endswith("r"))

# to capitalize the first letter of the string
print(str.capitalize())
# however the capitalization works only once, as in, it doesnt change the original string.. 
# check the next example
print(str)

# if we want to change the original string, 
# we can reassign the variable to the capitalized version of the string
#str = str.capitalize()
#print(str)

# for the capitalize() method to capitalize the first letter of each word in the string
# we can use the title() method.
print(str.title())

# replacing a substring in the string with another substring
print(str.replace("coder","programmer"))
print(str) 
# the original string remains unchanged, 
# as the replace() method returns a new string with the replaced substring.

# using find function to find the index of a substring in the string
print(str.find("o"))

# the output will return -1 if the substring is not found in the string
print(str.find("z"))

# count the number of occurrences of a substring in the string
print(str.count("a"))

# using the split() method to split the string into a list of substrings based on a delimiter
print(str.split(" "))

# using the join() method to join a list of substrings into a single string with a specified delimiter
list_of_words = ["I", "am", "a", "programmer"]
print(" ".join(list_of_words))

"""
there are many more string methods available in Python,
you can check the official documentation for a complete list of string methods and their usage.
simply type your string variable followed by a dot 
and then press the tab key to see a list of available methods for that string variable.
"""