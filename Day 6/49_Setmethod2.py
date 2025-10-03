collection = ({1,2,3,4,5})
print(len(collection))

#3 set.clear() : clears the element from the set

collection.clear()
print(len(collection))

collection1 = {"hello","ishani","ranwadkar"}

#4 set.pop() : pops any of the elements present in the set randomly

print(collection1.pop())

#5 set.union(set2)
set1 = {1,2,3,4,5}
set2 = {2,3,4,6,7}
print(set1.union(set2))
print(set1)#the values do not change 
print(set2)

#6 set.intersections(set2)

set1 = {1,2,3,4}
set2 = {2,3,5,6,7,8}
print(set1.intersection(set2))