# Q1) Write a program in which you have to ask S1, S2, S3 and show the output in this way:
# [(S1|S2)|S3] 


S1_1=input('Enter your S1: ')
S1_2=input('Enter your S2: ')
S1_3=input('Enter your S3: ')
print('[(',S1_1,'|',S1_2,')|',S1_3,']', sep='')


# Q2) Write a program in which you have to ask S1, S2, S3 and show the output in
# this way: [(S1,S2|S2/S1)||S3||] 


S2_1=input('Enter your S1: ')
S2_2=input('Enter your S2: ')
S2_3=input('Enter your S3: ')
print('[(',S2_1,',',S2_2,'|',S2_2,'/',S2_1,')||',S2_3,'||]', sep='')


# Q3) Write a program in which you have to ask S1, S2, S3, S4
# and show the output in this way: [[S1]/\[S2]/\[S3]/\[S4]] 


S3_1=input('Enter your S1: ')
S3_2=input('Enter your S2: ')
S3_3=input('Enter your S3: ')
S3_4=input('Enter your S3: ')
print('[[',S3_1,']/\[',S3_2,']/\[',S3_3,']/\[',S3_4,']]', sep='')



# Q4) Write a program in which you have to
# ask S1, S2, S3, S4 and show the output in this way: |S1|-->S2<--|S3|-->S4 


S4_1=input('Enter your S1: ')
S4_2=input('Enter your S2: ')
S4_3=input('Enter your S3: ')
S4_4=input('Enter your S3: ')
print('|',S4_1,'|-->',S4_2,'<--|',S4_3,'|-->',S4_4, sep='')


# Q5) Write a program in which you have to ask S1, S2, S3, S4 and show the output in this way: 
# |S1|/-\|->S2<-|/-\|S3|/-\|->S4 

S5_1=input('Enter your S1: ')
S5_2=input('Enter your S2: ')
S5_3=input('Enter your S3: ')
S5_4=input('Enter your S4: ')
print('|',S5_1,'|/-\\|->',S5_2,'<-|/-\\|',S5_3,'|/-\\|->',S5_4, sep='')


# Q6) Write a program in which you have to ask S1, S2, S3, S4, S5 and show the output in
# this way: S1|?|S5-~>S3$#>_[S2|(S4]] 

S6_1=input('Enter your S1: ')
S6_2=input('Enter your S2: ')
S6_3=input('Enter your S3: ')
S6_4=input('Enter your S4: ')
S6_5=input('Enter your S5: ')
print(S6_1,'|?|',S6_5,'-~>',S6_3,'$#>_[',S6_2,'|(',S6_4,']]', sep='')



# Q7) Write a program in which you have to ask S1, S2, S3,
# S4, S5 and show the output in this way: S1S2S3S4S5S2S3S1S4S1S2S4S5 

S7_1=input('Enter your S1: ')
S7_2=input('Enter your S2: ')
S7_3=input('Enter your S3: ')
S7_4=input('Enter your S4: ')
S7_5=input('Enter your S5: ')
print(S7_1,S7_2,S7_3,S7_4,S7_5,S7_2,S7_3,S7_1,S7_4,S7_1,S7_2,S7_4,S7_5 ,sep='')



# Q8) Write a program in which you have to ask S1, S2, S3, S4, S5 and show the output in this way:
#  [S1/|\(|S2|(|S3|)/|\S4|)||S5] 

S8_1=input('Enter your S1: ')
S8_2=input('Enter your S2: ')
S8_3=input('Enter your S3: ')
S8_4=input('Enter your S4: ')
S8_5=input('Enter your S5: ')
print('[',S8_1,'/|\(|',S8_2,'|(|',S8_3, '|)/|\ ',S8_4,'|)||',S8_5,']', sep="")



# Q9) Write a program in which you have to ask S1, S2, S3 and show the
# output in this way: (|S1-><-S2|]<>><<>[[[S3]]] 

S9_1=input('Enter your S1: ')
S9_2=input('Enter your S2: ')
S9_3=input('Enter your S3: ')
print('(|',S9_1,'-><-',S9_2,'|]<>><<>[[[',S9_3,']]]', sep="")


# Q10) Write a program in which you have to ask
# S1, S2, S3 and show the output in this way: (((S1S3||/-?||S2,S1||?-\/||S3S2]]] 

S9_1=input('Enter your S1: ')
S9_2=input('Enter your S2: ')
S9_3=input('Enter your S3: ')
print('(((',S9_1,S9_3,'||/-?||',S9_2,',',S9_1,'||?-\/||',S9_3,S9_2,']]]', sep="")


# Q11) Write a program to draw All Capital English Alphabets shapes using "*": * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * . . . * * * * * * * * * * * * 

print("  *  \n * * \n*   *\n*****\n*   *\n*   *\n")
print("**** \n*   *\n**** \n*   *\n**** \n")
print("**** \n*\n*\n*   \n**** \n")