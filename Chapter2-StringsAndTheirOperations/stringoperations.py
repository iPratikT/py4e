# in this program, we will demonstrate how to perform basic string operations in Python.

str1,str2 = "Hello", "World"

# Concatenation
result = str1 + " " + str2
print("result:",result)

# length
print("the length of the string is:",len(result))

# Repetition
repetition = result * 3
print("repetition:",repetition)

# Slicing
""" this will be used a lot during machine learning and data science,
 so it is important to understand how to use it."""
slicing = result[1:4]
print("slicing:",slicing)
print("printing using the length of the string:",result[6:len(result)])
print("printing using negative indexing:",result[-5:-1])
print("printing while missing the start index:",result[:5])
print("printing while missing the end index:",result[6:])

# Uppercase and Lowercase
print("upper case:",result.upper())
print("lower case:",result.lower())

# Stripping whitespace
str_with_whitespace = "   Hello World   "
print("string with whitespace:",str_with_whitespace)
print("string without whitespace:",str_with_whitespace.strip())

# Splitting and Joining
split_str = result.split(" ")
print("split string:",split_str)
joined_str = "-".join(split_str)
print("joined string:",joined_str)

# Checking if a substring exists
substring_check = "Hello" in result
print("substring exists:",substring_check)

# indexing
print("first character:",result[0])  # First character
print("last character:",result[-1])  # Last character
