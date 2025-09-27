name  = input( "enter your name : ")
age  = input ("enter your age : ")
marks  = input ("enter your marks : ")

print (name)
print(age)
print(marks)

# wrong way to print the type of variables

print(type(name))
print(type(age))
print(type(marks))

name  = input( "enter your name : ")
age  = int(input ("enter your age : "))
marks  = float(input ("enter your marks : "))

# right way to print the type of variables

print(type(name))
print(type(age))
print(type(marks))