##arr=[]
##arr=[1,2,3,4,5,6]
##def array(arr):
##    sum=0
##    for i in arr:
##        sum = sum + i
##    return(sum)
##a = len(arr)
##print ('Sum of the array is ',(array (arr)))
    
##name = 'World'
##program = 'Python'
##print(f'Hello {name}! This is {program}')
##
##name = 'world'
##program ='python'
##print('Hello %s! This is %s.'%(name,program))
##
##a="wasim"
##b="python programmer"
##print(f"my name {a}! is the {b}  ")
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
   
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
