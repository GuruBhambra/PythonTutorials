# loops in python
# list1 = [int,1,2,3,4,5,6,7,8,9,0, "we"]
# for item in list1:
#     if str(item).isnumeric() and item>6:
#         print(item)

# i=0
# while(i<20):
#     print(i)
#     i=i+1
list1 = ["int",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"we"]

# item = 0
# while(item<len(list1)):
#     if str(list1[item]).isnumeric() and list1[item]>6:
#         print(list1[item])
#     # print(list1[item])
#     # print(item)
#     item = item +1

# for i in list1:
#     if str(i).isnumeric() and i>6:
#         print(i)

# item = 0
# while(item<len(list1)):
#     if str(list1[item]).isnumeric() and list1[item]>6:
#         print(list1[item])
#     item = item + 1
# num = 0
print("Enter the number:- ")

while(True):
    num = int(input())
    if(num<100):
        continue


    elif(num >100):
        break

print("executed!")
