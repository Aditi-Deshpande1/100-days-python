# List method

list = [1,2,3,4,5,6]

list.append(7) #adds 7 at the end of the list
print(list)

list.sort() #sorts the list in ascending order
print(list)

list.reverse() #reverse of the list
print(list)

list.sort(reverse  = True)  #sorts the list in descending order
print(list)

list.insert(2,2.5) #inserts 2.5 at index 2 . Format : list.insert(index,element)
print(list)

list.remove(2.5) #remove 2.5 from the list
print(list)

list.pop(3) #removes element st index 3
print(list)
