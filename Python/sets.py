# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

# Remove elemnt from set
s.remove(5)
print(s)

#added Frozen set
fs=frozenset(["a","b","c"])
print(fs)

#Union an Itersection of sets
s=set([1,2,3,4])
s1=set([3,4,5,6])
print(f"set1 is {s} and set2 is {s1}")
#union
print(f"Union is {s|s1}")
#intersection
print(f"Intersection is {s&s1}")
