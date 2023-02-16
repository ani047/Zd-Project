'''
Write a program to extract numbers from a gien string
Input :- red 12 black 45 green
Output :- [12, 45]
'''
s1 ='red 12 black 45 green'
s2 = s1.split()
temp = []
for i in range(len(s2)):
    if((s2[i]).isdigit()):
      temp.append(int(s2[i]))
print(temp)  