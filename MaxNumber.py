# Write a Python function to find the Max of three numbers

def maxNum(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

max = maxNum(num1, num2, num3)
print("Maximum Number amoung of three number is = ", max)
