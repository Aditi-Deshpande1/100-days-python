#Dictionary method


info = {
    "name" : "Aditi",
    "age" : "17",
    "subject" : "Python",
    12.99 : "94.4"
}

print(info.keys())#1 info.keys() : returns all keys 

info = {
    "name" : "Aditi",
    "Subjects" : {
        "phy" : 94,
        "chem" : 93,
        "maths" : 92,
    }
}
print(info.keys())
print(len(info))

print(info.values())#2 info.values() : returns all values

print(list(info.items()))#3 info.items() : return all values and keys
pairs =  list(info.items())
print(pairs[0])
print(pairs[1])


print(info.get("name"))#4 returns the key according to value

#print(info["name2"])#error
#print(info.get("name2"))#no error -> None

info.update({"city" : "pune"})
print(info)

student = {
    "name" : "Shraddha kapra",
    "subjects" : {
        "phy" : 94,
        "chem" : 93,
        "math" : 92
    }
     }
   
new_dict = {"name" : "neha kumar", "age" : 17}
student.update(new_dict)

print(student)