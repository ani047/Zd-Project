'''
write a program to split a list every nth element
Input :-
['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

Output :-
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
'''

list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
n=3
print([list1[i::n] for i in range(n)])