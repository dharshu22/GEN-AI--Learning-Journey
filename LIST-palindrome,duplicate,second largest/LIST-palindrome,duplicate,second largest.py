#Given string is palindrome or not:
string = input("Enter a string:")
reverse =""
for i in string:
    reverse = i+reverse
if string ==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

print("--------------------------")

#second-largest number in a list of integers.
numbers = [22,8,5,21,20]
print("Second largest number:")
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers)>=2:
    second_largest = unique_numbers[-2]
    print(second_largest)
else:
        print("It doesn't have a second-largest number")
print("-------------------------")

#Remove all duplicate elements from a list and print the updated list.
org_list = ["Vijay","surya","Siva","Vijay","Atharvaa"]
print("update_list:")
for i in org_list.copy():
    while org_list.count(i)>1:
        org_list.remove(i)
print(org_list)

