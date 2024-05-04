# 1) Swap the values of 2 variables, using arithmetic operators."
# In this context, "swap" means exchanging the values of two variables, and "arithmetic operators"
# refer to mathematical operations such as multiplication and divison that are used to perform calculations
# in programming languages.

a=2
b=3
print("Before Swap",a,b)
a=a*b
b=int(a/b)
a=int(a/b)
print('After Swap',a,b)

# 2) Write a Python program that, if you are sitting in this rectangular room and you don't know its area, you
# should generate a program to find its area when its length and width are known."


l=int(input('Enter length of room: '))
w=int(input('Enter width of room: '))
a=l*w
print('Area of room is',a)

# 3) Write a Python program to take input from the user. If the user gives a negative value, it should become
# positive, and if the user gives a positive value, it should become negative."

a=int(input('Enter any Integer: '))
print(a)
a=-a
print(a)

# 4) Write a python program, suppose a student who has taken exams for 8 subjects but does not know how
# to calculate the average. So, could you create a Python program where the student enters their marks and
# the average is calculated?

a=int(input('Enter marks of subject 1: '))
b=int(input('Enter marks of subject 2: '))
c=int(input('Enter marks of subject 3: '))
d=int(input('Enter marks of subject 4: '))
e=int(input('Enter marks of subject 5: '))
f=int(input('Enter marks of subject 6: '))
g=int(input('Enter marks of subject 7: '))
h=int(input('Enter marks of subject 8: '))
avg=(a+b+c+d+e+f+g+h)/8
print('Average of marks is',avg)


# QUESTION 5
L=2
z=3
c=5
h=(((L**3)**z)**2) + ((6**c)/(5**2))
print(h)


x=2
y=3
z=4
r=((x**2)+(y**z)) / (2**(x+(y**2)))
print(r)

z=2
c=3
s=(((((5**2)**4)**z)**3)**3) - ((6**c)-(4**4)/(c**4))
print(s)
