# Q5) Write a python program to do these conversions (Add comments before each conversion):

# 1) "23"         -> int()
s="23" 
i=int(s)
print(i, type(i))


# 2) "23.2"         -> float()
s="23.2"
f=float(s)
print(f, type(f))


# 3) 23.52         -> str()
f = 23.52
s = str(f)
print(s, type(s))


# 4) 41            -> float() + Add 2.6         -> int()
i=41
f=float(i) + 2.6
i=int(f)
print(i, type(i))


# 5) "55.2"        -> int() + Divide by 3.5    -> str()
s="55.2"
f=float(s)
i=int(f)
i=i/3.5
s=str(i)
print(s, type(s))


# 6) True (bool)        -> str()                    -> bool()
b=True
s=str(b)
b=bool(s)
print(b, type(b))


# 7) 1            -> float()                    -> int()    -> bool()
i=1
f=float(i)
i=int(f)
b=bool(i)
print(b, type(b))


# 8) 1            -> float() + Subtract 0.9    -> int()    -> bool()
i=1
f=float(i)
f=f-0.9
i=int(f)
b=bool(i)
print(b, type(b))


# 9) 5.5            -> str()                     -> int() + Divide by 5
f=5.5
s=str(f)
f=float(s)
i=int(f/5)
print(i, type(i))


# 10) "44"        -> int() + Add 5.5                 -> str()
s="44"
i=int(s) + 5.5
s=str(i)
print(s, type(s))