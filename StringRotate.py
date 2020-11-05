# Write a program to generate all rotations of given string
str = "indal"
size = len(str)
temp = str+str

for x in range(size):
    for y in range(size):
        print(temp[x+y], end=" ")
    print()
