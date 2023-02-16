'''
program to get a list,sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
Input :- [(2,5),(1,2),(4,4),(2,3),(2,1)]
Output :- [(2,1),(1,2),(2,3),(4,4),(2,5)]
'''
ambuj = [(2,5),(1,2),(4,4),(2,3),(2,1)]
amb=(sorted(ambuj, key=lambda x:x[1]))
print(amb)