a = input("Enter your first movie : ")
b = input("Enter your second movie : ")
c = input("Enter your third movie : ")

list = [a , b ,c]

print("List  : ",list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)