'''
Given an array A your task is to tell at which position the equilibrium first occurs in the array.Equilibrium position
in an array is a position such that the sum of elements below it is equal to the sum of elements
after it.'''
x=int(input())
l=[]
list2=[]
def f(arr,high,low):
    bsum=0
    msum=0
    mid=(low+high)//2
    bsum=sum(arr[0:mid])    
    msum=sum(arr[mid+1::])
    if bsum==msum:
        print(mid+1)
        return 0
    elif bsum>msum:
        high=mid
        return f(arr,high,low)
    elif bsum<msum:
        low=mid
        return f(arr,high,low)
    else:
        if(mid==high or mid==low):
            return 0
for i in range(x):
    y=int(input())
    list1=[int(x) for x in input().split(" ")]
    l.append(y)
    list2.append(list1)
for j in list2:
    high=len(j)-1
    low=0
    f(j,high,low)        
    


