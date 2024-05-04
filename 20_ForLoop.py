# Table of 2
for i in range(1, 11):
    print("2 x", i, "=", 2*i)

# DingDong
a=int(input("Enter a starting number: "))
b=int(input("Enter a ending number: "))

for i in range(a,b):
    if (i%3==0 and i%5==0):
        print (i, "DingDong")
    elif (i%3==0):
        print (i, "Ding")
    elif  (i%5==0):
        print (i, "Dong")
    
# Squaring and Cubing
a=int(input("Enter a starting number: "))
b=int(input("Enter a ending number: "))
print("Number     Square      Cube")
for i in range(a, b):
    print(i,"         ",i**2, "        ", i**3)


# Even and Odd
a=int(input("Enter a starting number: "))
b=int(input("Enter a ending number: "))
for i in range(a,b):
    if (i%2==0):
        print("Even:", i)
    else:
        print("Odd: ", i)

import math 

a=int(input("Enter a starting number: "))
b=int(input("Enter a ending number: "))
print('Number     Factorial')
for i in range(a,b):
    print(i,"        ",math.factorial(i) )