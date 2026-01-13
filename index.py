# name = input("What is your name:")
# age = int (input("Enter your age"))

# print("Hello", name)
# print("My age is ", age)

# (wrong code ) Num1 = int(input ("Enter number 1:"))
# Num2 = int(input ("Enter number 2:"))
# sum = Num1 + Num2
# sub = Num1 - Num2
# print("Addition", sum)
# print("Substraction", sub)

# a=10
# b=6

# print("add", a+b)
# print("sub", a-b)
# print("mul", a*b)
# print("div", a/b)
# print("mod", a%b)
# print(a//b)
# print(a**b)

# for i in range (1,8,2): print(i)

# for i in range (0,9,2): print(i)

# num = int (input("Enter a number:"))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num //10

# if original == reverse :
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# print(121 == int (str(121) [: : -1]))

# s=0
# n=153
# old = n

# while n!=0 :
#     d = n%10
#     s=s+d*d*d
#     n= n//10

# if old == s:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong number")


# a=10
# b=5
# def add(a,b):
#     return a+b
# c = add(a,b)
# print (c)

# tuple1 ={1,2,3,4}
# tuple2 ={5,6,7,8}
# print(id(tuple1), id(tuple2))

# import copy
# a=[[1,2],[3,4]]
# b=a.copy()

# c = copy.deepcopy (a)
# a[0][0]=15
# a[0][1] =12
# print("a:",a)

# print("b:",b)
# print("c:",c)

import string
import random

print("password generation")

n=int(input("Enter the length of password:" ))
c = string.ascii_letters + string.digits + string.punctuation
p = " ".join (random.choice(c) for i in range (n))

print("Your password is:", p)
