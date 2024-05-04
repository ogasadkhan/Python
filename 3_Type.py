# Exercise 1: Variable Declaration
# Declare three variables: one integer, one float, and one string. Assign any values of your choice to
# these variables.

a1=10
b1=3.141
c1="Asad"



# Exercise 2: Variable Swapping
# Swap the values of two variables without using a third variable.

a2= 10
b2=30
print("Before Swapping",'a=',a2,'b=',b2)
a2,b2=b2,a2
print("After Swapping",'a=',a2,'b=',b2)



# Exercise 3: Data Type Conversion
# Convert the following:
# Convert an integer to a float.
# Convert a float to an integer.
# Convert an integer to a string.

a3=float(30)
print(type(a3))
b3=int(3.141)
print(type(b3))
c3=str(30)
print(type(c3))


# Exercise 4: String Concatenation
# Create two strings and concatenate them together using the + operator.

a4="Asad"
b4="Khan"
print(a4+b4)


# Exercise 5:
# Create a Python program to find the lengths of 2 strings as a input from the user, then concatenate
# those lengths
a5=input("Enter first string:")
b5=input("Enter second string:")
c5=str(len(a5))
d5=str(len(b5))
print(c5+d5)



# Exercise 6:
# Create a  Python program to demonstrate different data types (int, float, string, complex) and 
# display their types.
a6=10
b6=20.90
c='Asad Khan'
d=complex(3,5)
print(type(a6), type(b6), type(c), type(d))


# Exercise 7:
# Create a Python program to create a sequence of data types and take input from the user for each data
# type. Then, display below the user's input to show which data type it belongs to.
a7=int(input("Enter any Integer:"))
b7=float(input("Enter any Float:"))
c7=input("Enter any String: ")
print(a7, type(a7))
print(b7, type(b7))
print(c7, type(c7))

