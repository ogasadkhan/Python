# # ASADULLAH KHAN

# Logical Operators
# M= (A+B)CD
a,b,c,d = 0,1,0,1
M = (a or b) and c and d
print(M)


# N = ABC(D+A)
a,b,c,d = 0,1,0,1
N = a and b and c and (d or a)
print(N)


# O = A'B+C'D'+(F')'
a,b,c,d,f = 0,1,0,1,0
O = ((not a) and b) or ((not c) and d) or (not f)
print(O)


# D = (A+B')'C'+(DA')'+B
a,b,c,d = 0,1,0,1
D = (not (a or (not b)) and c) or (d and (not a)) or b
print(D)


# L = AB(C(D+A'))'+B'A'
a,b,c,d = 0,1,0,1
L = (a and b) and (not (c and (d or (not a)))) or ((not b)  and (not a))
print(L)


# H = (A+B+C) + (D')'C
a,b,c,d = 0,1,0,1
H = (a or b or c) or ((not (not d)) and c)
print(H)



# # G = ABCD + (A'B'C'D')'
a,b,c,d = 0,1,0,1
G = (a and b and c and d) or (not ((not a) and (not b) and (not c) and (not d)))
print(G)


# Z= (P+Q)+UW
p,q,u,w = 0,1,0,1
Z = (p or q) or (u and w)
print (Z)


# R= (P'+U')(U+W)
p,q,u,w = 0,1,0,1
R = ((not p) or (not u)) and (u or w)
print(R)



# T= Q(PQ')(QP)PQ'
p,q,u,w = 0,1,0,1
T = (q and (p and (not q))) and (q and p) and (p or (not q))
print(T)


# O = A'B'C'D'(F')'
a,b,c,d,f = 0,1,0,1,0
O = ((not a) and (not b) and (not c) and (not d) and (not (not f)))
print(O)


# G = (A+B+C+D)(A'B'C'D')'
a,b,c,d,f = 0,1,0,1,0
G =  ((a or b or c or d) and (not((not a) and (not b) and (not c) and (not d))))
print(G)


a=10
b=3
print(a or b)