# 1) If the user provides 3 inputs (name, city, and age), and if the age is 18 or above, 
# the user is eligible to obtain an NIC card. 
# If the user is 18 or below, they are not eligible.
print("Question 1")
name=input('Enter your name: ')
city=input('Enter your city: ')
age=int(input('Enter your age: '))

if age >= 18:
    print(name, 'is eligible to obtain an NIC card')
else:
    print(name, 'is not eligible to obtain an NIC card')


# 2) Gizmo was a student who was anxious about his university admission, whether he would 
# pass or fail. In this situation, to create a Python program, Gizmo needs to input the 
# obtained marks and total marks. After calculating the percentage, it can be determined 
# whether Gizmo has passed or failed. If Gizmo's marks are 70 or above, he is considered 
# to have passed, and if they are below 70, he is considered to have failed.
print("\nQuestion 2")
obtained_marks=int(input('Enter Gizmos obtained marks: '))
total_marks=int(input('Enter total marks: '))
percentage=(obtained_marks/total_marks)*100
print("Gizmo's percentage is",percentage)
if percentage >= 70:
    print('Gizmo has passed')
else:
    print('Gizmo has failed')




# Q1) Write a program to ask a user for his name, if the name length is greater than 10, 
# print 'FINE' otherwise 'TRY AGAIN'
print("\nQuestion 3")

name=int(len(input('Enter your name: ')))
if name > 10:
    print('FINE')
else:
    print('TRY AGAIN')


# Q2) Write a program to ask two numbers from the user, add them and multiply them and
# save their results in 2 variables. If their result is same it should print "PERFECT" 
# otherwise "GOOD"

print("\nQuestion 4")
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=a+b
d=a*b
if c == d:
    print('PERFECT')
else:
    print('GOOD')



# Q3) Write a program to ask user for his CNIC number, if the number entered by the user
# contains "-" then print "VALID" otherwise "INVALID"
print("\nQuestion 5")
nic_no=input('Enter your CNIC number: ')
if '-' in nic_no:
    print('VALID')
else:
    print('INVALID')


# Q4) Write a program to ask user for his name and age. If the age is greater than 18 
# and name is not empty, then print "ELIGIBLE" otherwise "TRY AGAIN"
print("\nQuestion 6")
a=input('Enter your name: ')
b=int(input('Enter your age: '))
if a != '' and b > 18:
    print('ELIGIBLE')
else:
    print('TRY AGAIN')
