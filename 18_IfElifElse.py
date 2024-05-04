# # QUESTION 1
print("QUESTION 1")
a=int(input('Enter an integer number: '))
if a%2==0:
    print('The number is even')
else:
    print('The number is odd')


# # QUESTION 2
print("QUESTION 2")
b=int(input('Enter a number: '))
if b==1:
    print('Monday')
elif b==2:
    print('Tuesday')
elif b==3:
    print('Wednesday')
elif b==4:
    print('Thursday')
elif b==5:
    print('Friday')
elif b==6:
    print('Saturday')
elif b==7:
    print('Sunday')
else:
    print('Invalid input')

# # QUESTION 2
print("QUESTION 3")
password = 'admin'
p=input('Enter password:')
p=p.lower()
if p==password:
    print('Password is correct')
else:
    print('Password is incorrect')


# # QUESTION 2
print("QUESTION 4")
s1=int(input("Enter first side of triangle: "))
s2=int(input("Enter second side of triangle: "))
s3=int(input("Enter third side of triangle: "))
if s1==s2==s3:
    print("Equilateral triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")