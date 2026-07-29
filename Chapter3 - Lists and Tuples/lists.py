# Creating a list
my_list = [1.22, 2.33, 3.44, 4.55, 5.66]

student = ["Alice", 21, "21.67"]

print("length of my_list:", len(my_list))

# Accessing elements of a list
student[0] = "Karan"

print ("Updated student list:", student)
print(type(student))
print(type(student[2]))


## Adding elements to a list
my_list.append(6.77)
print("Updated my_list:", my_list)

# Removing elements from a list
my_list.remove(2.33)
print("Updated my_list after removing 2.33:", my_list)

## Slicing a list
print("Slicing my_list from index 1 to 3:", my_list[1:4])
print("Slicing my_list from reverse:", my_list[-3:-1])

# sorting a list
my_list.sort()
print("Sorted my_list (usually in ascending order):", my_list)

# sorting a list in descending order
my_list.sort(reverse=True)
print("Sorted my_list (in descending order):", my_list)

# lets see if sorting a list of strings works
names = ["Charlie", "David", "23", "Bob"]
names.sort()
print("Sorted names (in ascending order):", names)

# reversing a list
names.reverse()
print("Reversed names:", names)
# apparently, the reverse() method does not sort the list in descending order, 
# it just reverses the order of the elements in the updated list (list after sorting). 

# inserting an element at a specific index
my_list.insert(2, 3.33)
print("Updated my_list after inserting 3.33 at index 2:", my_list)

# removing an element at a specific index
del my_list[3]
print("Updated my_list after deleting element at index 3:", my_list)

# removing an element at a specific index using pop()
popped_element = my_list.pop(2)
print("Popped element at index 2:", popped_element)
print("Updated my_list after popping element at index 2:", my_list)
