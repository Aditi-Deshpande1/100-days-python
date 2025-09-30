#Palindrome

original =  [1,2,2,1]

print(original)

reverse = original.copy()
reverse.reverse
print(reverse)

if(original ==  reverse):
    print("Palindrome")
else:
    print("Not a Palindrome")

