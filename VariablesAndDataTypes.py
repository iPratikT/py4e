name = 'Pratik Tabhane'
type1 = type(name)
print("name is", type1, "and its value is", name )

age = 35
type2 = type(age)
print("age is", type2, "and its value is", age )

price = 100.50
type3 = type(price)
print("price is", type3, "and its value is", price )


# now lets see if we can add age and price
total = age + price
print("total is", total)

# boolean data type
is_adult = True
type4 = type(is_adult)
print("is_adult is", type4, "and its value is", is_adult )

# next lets check the data type of a list
my_list = [1, 2, 3, 4, 5]
type5 = type(my_list)
print("my_list is", type5, "and its value is", my_list )

# next lets check the data type of a tuple
my_tuple = (1, 2, 3, 4, 5)
type6 = type(my_tuple)
print("my_tuple is", type6, "and its value is", my_tuple )

# next lets check the data type of a set
my_set = {1, 2, 3, 4, 5}
type7 = type(my_set)
print("my_set is", type7, "and its value is", my_set )

# next lets check the data type of a dictionary
my_dict = {'name': 'Pratik', 'age': 35, 'price': 100.50}
type8 = type(my_dict)
print("my_dict is", type8, "and its value is", my_dict )

# next lets check the data type of a None
my_none = None
type9 = type(my_none)
print("my_none is", type9, "and its value is", my_none )

# next lets check the data type of a complex number
my_complex = 1 + 2j
type10 = type(my_complex)
print("my_complex is", type10, "and its value is", my_complex )

# next lets check the data type of a bytes
my_bytes = b'Hello'
type11 = type(my_bytes)
print("my_bytes is", type11, "and its value is", my_bytes )

# next lets check the data type of a bytearray
my_bytearray = bytearray(b'Hello')
type12 = type(my_bytearray)
print("my_bytearray is", type12, "and its value is", my_bytearray )

# next lets check the data type of a memoryview
my_memoryview = memoryview(b'Hello')
type13 = type(my_memoryview)
print("my_memoryview is", type13, "and its value is", my_memoryview )

# next lets check the data type of a range
my_range = range(5)
type14 = type(my_range)
print("my_range is", type14, "and its value is", my_range )

# next lets check the data type of a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
type15 = type(my_frozenset)
print("my_frozenset is", type15, "and its value is", my_frozenset )