#Syntax of Python

print("Ambuj Namdev")
am =['Ambuj','NOTHING','Break','GOOD']
def func():
 a=10    
 for i in range(5) :
    b=a
    c=a+b
    print(c)
    a=a+5
func()

for e in am :
    print(e)

name="Ambuj Namdev"
print("Name = ",name,sep='Mr ',end=' Ji')

name= input("Enter The Name ")
print("Name = ",name,sep='Mr ',end=' Ji') 

a= int (input("enter first number: "))
b= int (input("enter second number: "))
print(a+b)
print(type(a))

ambuj =["LIST","AMBUJ"]
amb=("TOUPLE","AMBUJ")
ambu={"SET","AMBUJ"}
amm={"Type":"Dictonary","Name":"AMBUJ"}
f=set(amb)
print(ambuj)
print(amb)
print(ambu)
print(amm)
print(type(ambuj))
print(type(amb))
print(type(ambu))
print(type(amm))
print(f)
print(type(f))

str = "Ambuj"
print (str)

li = [2]
li.append(5)
li.append(10)
print("Adding 5 and 10 in list", li)
li.pop()
print("Popped one element from list", li)
print()

s = set()
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
s.remove(5)
print("Removing 5 from set", s)
print()

t = tuple(li)
print("Tuple", t)
print()

d = {}
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
del d[10]
print("Dictionary", d)

g="   Ambujasas  "
print(g.strip())