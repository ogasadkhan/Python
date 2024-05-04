# ASADULLAH KHAN

# 1) If the user provides 3 inputs (name, city, and age), and if the age is 18 or above, the user is eligible to obtain an NIC card. 
# If the user is 18 or below, they are not eligible.
print("Question 1")
name = input("Enter your name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name ," is eligible to obtain an NIC card.")
else:
    print(name ," is not eligible to obtain an NIC card.")


# 2) Gizmo was a student who was anxious about his university admission, whether he would pass or fail. In this situation, to create a Python program, Gizmo needs to input the obtained marks and total marks. After calculating the percentage, it can be determined whether Gizmo has passed or failed. If Gizmo's marks are 70 or above, 
# he is considered to have passed, and if they are below 70, he is considered to have failed.
print("\nQuestion 2")
obtained_marks = int(input("Enter Gizmo obtained marks: "))
total_marks = int(input("Enter the total marks: "))

percentage = (obtained_marks / total_marks) * 100
print("Gizmo's percentage is", percentage)
if percentage >= 70:
    print("Gizmo has passed!")
else:
    print("Gizmo has failed.")
