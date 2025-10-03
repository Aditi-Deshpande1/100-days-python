#Set itself is mutable 
#while the element it the set in not mutable they are immutable

#1 : set.add(el) =  add an element
collection  = set ()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)
collection.add("Aditi Deshpande")
collection.add((1,2,3,4))
collection([1,2,3,4])

print(collection)
print(type(collection))

#2 : set.remove(el) =  removes an element 

collection.remove(1)
print(collection)