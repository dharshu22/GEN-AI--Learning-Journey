#sum of all elements in list:

numbers = [22,27,21,51,43]
list = 0
print("sum of elements:")
for i in numbers:
    list +=i
print(list)

#max of all elements in list:

numbers = [22,27,21,51,43]
max = numbers[0]
print("Max of elements:")
for i in numbers:
    if i>max:
        max = i
print(max)

#mini of all elements in list:

numbers = [22,27,21,51,43]
min = numbers[0]
print("Min of elements:")
for i in numbers:
    if i>min:
        min = i
print(min)

#average of all elements in list:

numbers = [22,27,21,51,43]
total = 0
print("Average of elements:")
for i in numbers:
    total += i
    average = total / len(numbers)
print(average)

# even numbers in given list:

numbers = [22,27,21,51,43]
total = 0
print("Even numbers:")
for i in numbers:
    if i%2 == 0:
        print(i)
