# Faulty Calculator

print("Please enter the first number:- ")
num1 = int(input())

print("Please enter the second number:- ")
num2 = int(input())

print("What operation you want to do with two numbers Here -> a is Add, s is Substract, d is Divide and m is Multiply")
opt = input()

if num1 == 45 and num2 == 3  or num1 == 45 and num2 == 3:
    print(555)

elif num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
    print(23)

elif num1 == 56 and num2 == 6 or num1 == 6 and num2 == 56:
    print(4)

elif opt == "m":
    sum = num1 * num2
    print(sum)
elif opt == "a":
    sum = num1 + num2
    print(sum)
elif opt == "s":
    sum = num1 - num2
    print(sum)
elif opt == "d":
    sum = num1 / num2
    print(sum)
