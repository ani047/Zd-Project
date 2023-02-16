'''
program to create a list by concatenating a given list which range goes from 1 to n.
Input :- ['p','q']
n = 5
Output :- ['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5'] 
'''
ambuj = ['p','q']
n = 5
amb = []
for i in range(1,n+1):
 for x in ambuj :
    amb.append(x+str(i))
print(amb)