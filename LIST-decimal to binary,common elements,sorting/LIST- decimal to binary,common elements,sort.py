#Decimal number to Binary num without any In-Built functions:
num = int(input("Enter a decimal number:"))
print("Decimal number to Binary:")
binary = ""
if num ==0:
    binary="0"
else:
    while num>0:
        remainder = num%2
        binary = str(remainder)+ binary
        num = num //2
print("Binary:",binary)


print("-------------------------------")
#Common elements in two lists
print("common elements in two list:")
list1 = [8,11,4,12,22]
list2 = [22,8,7,9,5]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print("Common elements:",common)


print("--------------------------------")
#Sort a list of strings in Alphabetical order
strings = ["orange","mango","apple","banana","strawberry"]
print("Sorting the list in Alphabetical Order:")
strings.sort()
print("Sorted list:",strings)


