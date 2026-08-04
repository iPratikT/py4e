something = {1,2,2,"hello","world","hello","hello"}

print(len(something))

something.add(3)
print(something)
something.remove(1)
print(something)

# something.add(3,"it is nice") -> if adding, or removing, only one at a time, else error

# randomly pop a value from the set
print("pop random value(s)", something.pop())

#clearing a set makes it an empty set
print(len(something))
something.clear()
print(something)

# learning union and intersection in a set -> works just like set theory of math

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #print all unique values of the union 
print(set1.intersection(set2)) #print all common values of the two sets