# Write a Python function to sum all the numbers in a list

def listSum(list):
    sum = 0
    for x in list:
        sum = sum+x
    return sum


list = [1, 5, 10, 4, 7]
sum = listSum(list)
print("Sum of List is = ", sum)
