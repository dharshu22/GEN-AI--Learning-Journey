#Remove spaces from given string:

s = input("Enter a string:")
print("Removing spaces from string:")
result = ""
for i in s:
    if i!=" ":
        result +=i
print("string without spaces:",result)
print("---------------------------------")


#Two string are anagram or not:

print("Given two strings are anagrams or not:")
str1 = input("Enter first string:")
str2 = input("Enter second string:")
s1 = sorted(str1.lower())
s2 = sorted(str2.lower())
if s1 == s2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
print("---------------------------------")

#Number of vowels in given string:

print("Number of vowels in given string:")
s = input("Enter a string:")
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count +=1
print("Number of vowels:",count)



