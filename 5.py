'''
Write a program to get a string made of the first two and last two, if less than 2 elements return Empty String 
Input :-'w3resouce' Output :- 'w3ce'
Input :-'w3' Output :- 'w3w3'
Input :-'w'  Output :- Empty String
'''
s1 ='w3resource'
#s1 ='w3ce'
#s1 ='w3'
#s1 ='w'

if(len(s1)>=2):
    print(s1[:2]+s1[-2:])
   
else:
     print("Empty String")
     