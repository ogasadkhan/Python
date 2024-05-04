# a={1,2,3}
# b={3,4,5}
# c=a.union(b)
# print(c)

# x={"name":"Asad", "age":20}
# y=x.
# print(type(x))

fruits={"apple":"Saib", "banana":"Kela", "mango":"Aam", "orange":"Narangi", "watermelon":"Tarbooz"}
# print(fruits.keys())
a=input("Enter a fruit: ").lower()

if a in fruits.keys():
    print("It is ",fruits[a])
else:
    print("Not found")