#File
# f = open("guru.txt")
# content = f.read(11)
# print("1",content)
#
# content = f.read(21)
# print("2",content)
# for line in f:
#     print(line)
# To print the content of the file line by line
# print(f.readline())
# print(f.readline())
# print(f.readline())

# To print the content of the line in set
# content = f.readlines()
# print(content)
# f.close()

# To write in the file

f = open("guru2.txt", "w")
content = f.write("Hello! How was ur day dear?\n")
a =f.write("It was a busy day?\n")
f.close()