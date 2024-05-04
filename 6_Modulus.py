a=20
b=43
c=2

print(a%c)  #0
print(b%c)  #1
#   (0+1)%2 = 1
ad=((a%c)+(b%c))%c
print(ad)

print(a%c)  #0
print(b%c)  #1
#   (0-1)%2 = 1
ad=((a%c)+(b%c))%c
print(ad)


print(a%c)  #0
print(b%c)  #1
#   (0*1)%2 = 1
ad=((a%c)*(b%c))%c
print(ad)


k=5
print(a%c)  #0
print(b%c)  #1
#   (0)**5 = 0
ad=((a%c)**k)%c
print(ad)

