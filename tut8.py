mystr = "guru are a good boy"
# print(mystr)

# print(len(mystr))
# print(mystr[0:18])#this will print the whole string
# print(mystr[0:18:2])#this will print the whole string by skipping each character
#
# print(mystr[10:13])
# print(mystr[::-1])

print("endswith",mystr.endswith("boy"))
print("alnum",mystr.isalnum())
print("alpha",mystr.isalpha())
print("count",mystr.count("g"))
print("find",mystr.find("good"))
print("upper",mystr.upper())
print("replace",mystr.replace("are", "is").upper())
print("Caps",mystr.replace("are", "is").capitalize())
print(mystr.encode())
print("upper",mystr.join("o"))
print("upper",mystr.strip("g"))
print("",mystr.rstrip("u"))