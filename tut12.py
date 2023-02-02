# Conditional Statements

"""

"""
print("Welcome to RTO Digital Age verification for License Apply")

print("Enter your age:- ")

age = int(input())

sum = 18-age

if age<7 or age>70:
    print("Thank You for your time but your age is not satisfactory for our policy")
elif age == 18:
    print("You need to report RTO for physical test if you need driving license at " + str(age))
elif age > 18:
    print("Congrats! You are eligible for driving license")
elif age<18 or age>7:
    print("Sorry! But you are not eligible for license right now. To apply for license you need have wait more " + str(sum)+ " years")






