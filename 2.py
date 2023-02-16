"""
    write a program to convert list to list of dictonary
    input :-
    ['black','red','maroon','yellow']
    ['#000000','#FF0000','#800000','#FFFF00']
    output :-
    [{'color_name': 'black', 'color_code': '#000000'},{'color_name': 'red', 'color_code': '#FF0000'}, 
    {'color_name': 'maroon', 'color_code': '#800000'},{'color_name': 'yellow', 'color_code': '#FFFF00'}]
"""

list1=['black','red','maroon','yellow']
list2=['#000000','#FF0000','#800000','#FFFF00']
list3 = []

for i in range(len(list1)):
    list3.append({'color_name': list1[i],'color_code':  list2[i] } )  
print(list3)