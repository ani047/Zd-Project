'''Write a program to remove duplicate words from string
 input :- Python Exercises Practice Solution Exercises
 output :- Python Exercises Practice Solution 
'''

s1 = 'Python Exercises Practice Solution Exercises'

split_list = s1.split()
temp=[]
for i in split_list:
 if i not in temp:
  temp.append(i)
print(' '.join(temp))
print(split_list)