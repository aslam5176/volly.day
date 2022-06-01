a=int(input("enter the number"))

def add(a,b):
  return a+b
print(add())
def mul(a,b):
return a*b
print(mul(a,b))
num1=add()+mul()
print(num1)

if(num1%5==0 and num1%6==0):
print("its divisible ")
else:
print("its not divisible ")
##def multiple(m, n):
##	return True if m % n == 0  else False
##
##print(multiple(20, 5))
##print(multiple(7, 2))
##def isDivisibleBy3(num):
##    if (num % 3) == 0:
##        return True
##    else:
##        return False
##print(isDivisibleBy3(15))
##print(isDivisibleBy3(6))
