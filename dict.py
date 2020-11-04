# Write a Python program to iterate over dictionaries function.

def displayDictionaryItem(dict):
    for x in dict:
        return x


d = {
    'key': "value",
    'num': 9,
    'name': "Indal Kumar"

}
disp = dict(d)
print(disp)


# display only key
print("Keys of dictionary")
for x in d.keys():
    print(x)

# display only values
print("Values of dictionary")
for x in d.values():
    print(x)
