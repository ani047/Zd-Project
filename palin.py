# Program for check number is palindrome or not !
# using floor division
n = int(input())
na = n
rev = 0
while (n > 0):
    d = n%10
    rev = rev*10 + d
    n = n // 10
if(na == rev):
    print("Number is palindrome!")
else:
    print("Not a palindrome!")

