#Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
#----------------------------------------------------------------------------------------------#
#simple one with O(n*n)
list1=[int(x) for x in input().split()]
p=int(input())
for i in range(len(list1)):
    sum=0
    for j in range(i,len(list1)):
        sum=sum+list1[j]
        if sum>p:
            break
        if sum==p:
            print(i+1,j+1)
            break
    if sum==p:
        break

#------------------------------------------------------------------------------------------------#
list1=[1,2,3,4,5,6,7,8,9]
sum=17
n=len(list1)
start=0
s=list1[0]
for i in range(1,len(list1)+1):
    while (s>sum and start < i-1 ):
        s=s-list1[start]
        start+=1
    
    
    if s==sum:
        print(start,i-1)
        break
    
    if i<n:
        s=s+list1[i]
#---------------------------------------------------------------------------------------------#
#efficient with O(n)
def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print ("Sum found between indexes")
            print ("%d and %d"%(start, i-1))
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
 
    print ("No subarray found")
    return 0
 
# Driver program
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
sum = 17
 
subArraySum(arr, n, sum)
 #--------------------------------------------------------------------------------------------------------#
 








