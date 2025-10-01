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

print(info.get("name"))