#Dictionary in python

"""
in dictionary the data values are stored in key and value pairs
dictionary are ordered, mutable and Do not allow duplicate values
in dictionary the key are case sensitive
though dictionary is a key value pair we can put the value as dictionary or list or tuple

"""
dict = {"A" : "Apple", "B" : "Boy", "C" : "Cat", "D" : "Dog"}
print(dict)
print(dict["B"])
x = dict.keys()
dict["E"] = "Eagle"
print(x)

dict["F"] = "Fan"
print(dict)