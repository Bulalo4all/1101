import re

#Context manager
with open('one_hundred.txt', 'r') as numbers:
    data = numbers.read()

#Creating and identifying numbers in document
items = re.split("\n| ", data)
items = set(items)
items.remove("")

intitems = [int(i) for i in items]

onehundred = []

#Creating a list of 1-100 to compare with document
for i in range(1,101):
    onehundred.append(i)

#iterating through the 1-100 and removing if int in document 
#to identify missing values from list
for i in range(1, 101):
    if i in intitems:
        onehundred.remove(i)

#sorted list of data items
outputlist = sorted(intitems)

# writing out to file with sorted list, new line created for
# every data piece
with open('one_hundred_sorted.txt', 'w') as output:
    for item in outputlist:
        output.writelines(str(item) + "\n")


