#Only the odd num in new list
numbers = [11,12,13,14,15,16,17]
odd_num = []
for i in numbers:
    if i %2 !=0:
        odd_num.append(i)
print("Original List:",numbers)
print("Odd Numbers List:",odd_num)
print("\n" + "*"*40)

#Reverse a list without built-in fun:

numbers = [22,21,8,5,21]
reversed_list = []
for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
print("Original List:",numbers)
print("Reversed List:",reversed_list)
print("\n" + "*"*40)

#List of integer into single integer:

numbers = [4,5,6,7,8]
single = 0
for i in numbers:
    single = single * 10 + i
print("Integer:",single)
