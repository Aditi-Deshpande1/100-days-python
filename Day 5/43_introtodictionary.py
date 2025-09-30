#Dictionary : used to store data values in key:value pairs
#They are unordered , mutuable(changable) & don't allow duplicate keys

dict = {
    "name" : "Aditi",
    "percentile" : "94.112",
    "learning" : "coding",
}
print(dict)

info = {
    "name" : "Aditi",
    "age" : "17",
    "subject" : "Python",
    12.99 : "94.4"
}

print(info)
print(type(info))
#key can be anything accept dict and set 

print(info["name"])
print(info["age"])
print(info["subject"])
print(info[12.99])

info["name"] = "Shraddha"#overwrite
info["age" ] =  25
print(info)

