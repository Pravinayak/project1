number=[10,30,40,50,6,33]
print(number[0:6:2])

#reversing the number
number.reverse()
print(number)

#sorting the number(ascending)

number.sort()
print(number)

#min number

print(min(number))

#max number

print(max(number))

#length of number
print(len(number))

#appending or adding the number in list (mostly it adds at the end of the list)

number.append(89)
print(number)

#inserting the value in list (first index is place and second index is value (2,101))
number.insert(3,101)
print(number)


#extend is useful to add more items in list
number.extend([78,66,88])
print(number)

#changing the value in list

number[2]=38
print(number)

#changing the more values in list
number[1:4]=[17,18,19]
print(number)

#removing the item from list
number.remove(50)
print(number)

#pop will remove the item from list from last

number.pop()
print(number)