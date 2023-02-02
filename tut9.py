# # # List  and tuples in python
# #
# # myList = ["apple", "watermelon","mango"]
# # print(myList)
# # myList.append("banana")
# # print(myList)
# #
# # myList.sort()
# # print(myList)
# # myList.append("banana")
# # print(myList)
# # myList.sort()
# # print(myList)
#
# # Extend list
# myNum = [1,2,3,4,5,6,7]
# num = [8,9,10]
# # # myNum.extend(num)
# # num.extend(myNum)
# # print(num)
# #
# # # Length List
# #
# # print(
# #     len(num)
# # )
# # remove
#
# # myNum.remove(2)
# # print(myNum)
# # del myNum[3]
# # print(myNum)
# # myNum.pop(2)
# # print(myNum)
# # myNum.clear()
# # print(myNum)
#
# # Loop in List
# myNum.extend(num)
# # for x in myNum:
#     # print(x)
#
#     # for i in range (len(myNum)) :
#         # print(myNum)
# #
# # i = 0
# # while i < len(myNum):
# #     print(myNum)
# #     i = i + 1
#
# # print(myNum)
#
#
# myFruits = ["Banana", "apple", "mango", "orange", "Watermelon"]
# # newFruits = [x for x in myFruits]
# newFruits = [x for x in range(10) if x< 7]
# # newFruits = []
# # for x in myFruits:
# #     if "n" in x:
# #         newFruits.append(x)
# print(newFruits)
#
# myNum.sort(reverse=True) # this method will sort the numbers from top to bottom
# myFruits.sort()
# print(myNum)
# print(myFruits)
# # myFruits.pop(3)
# # print(myFruits)
# myFruits.remove("mango")
# print(myFruits)


x = ("apple", "banana", "cherry")
y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

print(y)