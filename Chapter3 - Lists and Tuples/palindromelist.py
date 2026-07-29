# WAP to check if a given list is a palindrome or not.

list1 = [1, 2, 3, 2, 1]
list2 = list1.copy()
list2.reverse()

if list1 == list2:
    print("The given list is a palindrome.")
else:
    print("The given list is not a palindrome.")
