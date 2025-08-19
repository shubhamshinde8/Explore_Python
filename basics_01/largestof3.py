

num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))
num3=int(input("Enter 3rd Number : "))

if(num1>num2 and num1>num3):
    print(num1, " Is Largest Number ")
elif(num2>num1 and num2>num3):
    print(num2," Is Largest Number")
else:
    print(num3," Is Largest Number ")

