##a=[1,2,3,4,5]
##b=0
##print("the list is=>",str(a))
##for i in a:
##    b=b+1
##print("the length of the list=>",str(b))    

a=["the lion king"]
print("the original list is=>",str(a))
b=[sub.replace("the","-").replace("*","the").replace("-","*")for sub in a]
print("after change the list=>",str(b))
