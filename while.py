####a=int(input("enter the number"))
##while(a==4):
##    a+=2
##    print(a)


##a = int(input("Enter a number: "))
##b=len(str(a))
##c=0
##for i in str (a):
##    c +=int(i)**b
##print(c)
##if a== c:
##   print(a,"is an Armstrong number")
##else:
##   print(a,"is not an Armstrong number")
##a=123
##print (len(a))
##print(a)
a=int(input("enter the number"))
b=0
while(a>0):
    c=a%10
    b=(b*10)+c
    a=a//10
print(b)    
