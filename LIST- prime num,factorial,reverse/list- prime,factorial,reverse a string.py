#The given number is prime or not:
numbers = [2,3,4,5,6,7,8,9,10]
print("Given number is prime or not:")
for i in numbers:
    if i>1:
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            print(i,'is a prime number')
print("-------------------------")

#Factorial of given number:
numbers = [2,3,4,5]
print("Factorial of given number:")
for i in numbers:
    factorial = 1
    for j in range(1,i+1):
        factorial *= j
    print("Factorial of",i,"=",factorial)
print("----------------------------")

#Reverse a strin without using any built-in functions:

word = input("Enter a string:")
reverse =""
for i in word:
    reverse = i + reverse
print("Reversed String:",reverse)


