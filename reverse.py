##a=input("enter the number") 
##def reverse_value(a):
##return a[::-1]
##print(reverse_value(a))
a=input("enter the value ")

def palindrome(s):
     
    if (s==s[::-1]):
        return"it is paliandrome"
    else:
        return"it is not paliandrome"

print(palindrome(a))

 
