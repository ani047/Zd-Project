'''
Write a script to sort (Accending or descending) a dictonary by value.
'''
ambuj = {
    'Ambuj':'2002','Algun':'2002','Zecdata':'2003','Class':'2004','Mus':'2001','Barfi':'2005'
}
ambu = dict(sorted(ambuj.items(), key=lambda x:x[0]))
print(ambu)
