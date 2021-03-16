print("Enter your age: ")
age = int(input())
minimum_age = int(18)
if age not in range (80):
    print("People of this age are not allowed to drive. ")
elif age<minimum_age:
    print("You are not eligible for driving test.")
elif age==minimum_age:
    print("We are not sure about whether you can drive or not so please kindly visit us for the inspection.")
else:
    print("You are eligible for the driving test.")