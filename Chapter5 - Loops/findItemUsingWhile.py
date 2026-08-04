# to search for an item in a tuple using while loop

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

item = int(input("Enter the item to search: "))
i = 0
while i < len(tup):
    if tup[i] == item:
        print("Item",item,"found at index",i)
    else:
        print("on index",i,"item not found")
    i += 1
        