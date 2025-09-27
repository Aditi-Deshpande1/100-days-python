#Positive indexing

#slicing of string
str = "Aditi Deshpande"
ch  = str[1:4]

print (ch)

#Slicing : Accessing a range of characters in a string 
#str[starting index : ending index]
#ending index is always excluded
#str[1:4] it will include index 1,2,3 but not 4

str = "Apna college"
print(str[5:len(str)])#length of string is + 1 of the last index 

str = "Apna college"
print(str[5:])#if we do not provide ending index it will automatically assume till end of string 

str= "Apna college"
print(str[:4])#if we do not provide starttting index it will automatically assume from 0th index

#negative indexing

str ="Apple"
print(str[-3:-1])#it will print from index -3 to -1 excluding -1 