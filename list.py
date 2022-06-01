##a = int(input("enter a number => "))
##
##product = a**2
##s = 0
##
##
##for i in str(product):
##    s += int(i)
##    
##
##if(a == s):
##    print("It is a Neon Number")
##
##else:
##    print("It is not a Neon Number")


##a = 0
##
##while(a < 3):
##    a += 1
##    print(a)
##a=1234567899
##print(repr(a)[-1])
a = int(input("enter the number"))
b = a**2
c=0
while b:
   c=c+(b%10)
   b=b//10
   

if c==a:
    print(a,"is a neon number")
else:
    print(a,"it is not a neon number")
    
