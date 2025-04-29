my_set={}
print(type(my_set))

a = {1,2,3,4}
b = set()
b.add("apple")


print(type(a))
print(type(b))

set1={1,2,3,4}
set2={3,4,5,6}

#union
print(set1.union(set2))
print(set1|set2)

#intersection
print(set1.intersection(set2))
print(set1&set2)

#difference
print(set1.difference(set2))
print(set1-set2)

#symmetric difference
print(set1.symmetric_difference(set2))
print(set1^set2)

#functions
b.add(3)
print(b)

#remove
b.remove(3)
print(b)

#discard
b.discard("apple")
print(b)

b.discard(3)
print(b)


# max() min() #sum()
print(max(set1))
print(min(set1))
print(sum(set1))

#sorted
print(sorted(set2))
