# ASADULLAH KHAN 

# 1) Swap the values of 2 variables, using arithmetic operators."In this context, "swap" means
#  exchanging the values of two variables, and "arithmetic operators" refer to mathematical 
# operations such as (addition & subtraction) and (Multiplication & Division) that are used 
# to perform calculations in programming languages.

# Using Addition & Subtraction
a=10
b=100
print("Q1\nAddition & Subtraction:\nBefore swap:", a,b)
a=a+b 
b=a-b
a=a-b
print("After:",a,b)

# Using Multiplication and Division
a=10
b=100
print("\nMultiplication and Division:\nBefore:",a,b)
a=a*b 
b=a/b
a=a/b
print("After:",a,b)


# 2) Take a string as input from the user, calculate its length, and convert it into an integer.
# Then, perform addition, subtraction, multiplication, division and floor division using the 
# obtained integer.

print('\nQ2')
a=int(len(input('Enter String: ')))
print("Length of String:", a)
print("Addition by 10:",a+10)
print("Subtraction by 10:",a-10)
print("Multiplication by 10:",a*10)
print("Division by 10:",a/10)
print("Floor Division by 10:",a//10)

# 3) Write a program in which you have to add 2 random numbers and check if they are equal to 12 or not?
print('\nQ3')
i=int(input('Enter first number: '))
j=int(input('Enter second number: '))
print("First number is equals to 12? ",i==12)
print("Second number is equals to 12? ",j==12)

# 4) Write a program in which you have to multiply 3 numbers together and check if the first number is less
# than their multiplication result
print('\nQ4')
a=1
b=2
c=3
print("Is \'a\' less than (a*b*c)? ",a<(a*b*c))
 

# 5) Write a program in which you have to Add 2 numbers and check if they are less than and equal to the
# multiplication of those 2 numbers or not.
print('\nQ5')
a=2
b=2
add=a+b
mul=a*b
print("Is (add)", add, "is equals to (mul)", mul,"?",(add)==(mul))


# 6) Write a program to square a number and check if it is not equal to the actual number or not.
print('\nQ6')
a=1
print("\'1\' is not equals to its square...",(a**2) != a)

# 7) ASSOCIATIVE LAW
    # 1) (A+B)+C = A+(B+C) (Answer will be incremented by 2)
print('\nQ7 (a)')
a,b,c=1,2,3
x=(a+b)+c
y=a+(b+c)
print(x==y)
x+=2
print("Result after increment by 2: ",x)

    # 2) (AB)C = A(BC) (Answer will be decremented by -1)
print('\nQ7 (b)')
a,b,c=1,2,3
x=(a*b)*c
y=a*(b*c)
print(x==y)
x-=1
print("Result after decrement by 1: ",x)


# 8) DE MORGAN LAW
# 1) (A+B)'=A'B' (Answer will be incremented by -0)
print('\nQ8 (a)')
a,b=1,1
x=not (a or b)
y=(not a) and (not b)
print(x==y)
x-=0
print("Result after decrement by 0: ",x)



# 2) (AB)'=A'+ B' (Answer will be decremented by 0.5)
print('\nQ8 (b)')
a,b=1,1
x=not (a and b)
y=(not a) or (not b)
print(x==y)
x-=0.5
print("Result after decrement by 0.5: ",x)

