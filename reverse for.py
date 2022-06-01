##a=int(input("enter the number"))
##b=0
##for i in  str(a):
##    c=a%10
##    b=(b*10)+c
##    a=a//10
##print(b)    
##
##for a in range(6):
##    for b in range(0,6):
##        print((a+b)%2, end=" ")
##    print()
##
##            
count=1
for i in range(1,6):
    for b in range(0,6):
        if(count==1):
            print(count,end="")
            count-=1
        else:
            print(count,end="")
            count+=1
    print()       
