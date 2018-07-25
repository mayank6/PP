'''
Given a sequence of distinct numbers a1, a2, ….. an, an inversion occurs if there are indices i<j such that ai > aj .

For example, in the sequence 2 1 4 3 there are 2 inversions (2 1) and (4 3).

The input will be a main sequence of N positive integers. From this sequence, a Derived Sequence will be obtained using the following rule. The output is the number of inversions in the derived sequence.

Rule for forming derived sequence

An integer may be represented in base 6 notation. In base 6, 10305 is 1x64 + 3x62 + 5 =1409. Note that none of the digits in that representation will be more than 5.

The sum of digits in a base 6 representation is the sum of all the digits at the various positions in the representation. Thus for the number 1409, the representation is 10305, and the sum of digits is 1+0+3+0+5=9. The sum of digits may be done in the decimal system, and does not need to be in base 6

The derived sequence is the sum of the digits when the corresponding integer is represented in the base 6 form number will be expressed in base 6, and the derived sequence is the sum of the digits of the number in the base 6 representation.
'''

x=int(input())
list1=[int(x) for x in input().split(",")]
string=""

def dectohex(x):
    string=""
    while(x>0):
        r=str(x%6)
        x=x//6
        string+=r
    return string[::-1]

list2=[]
for i in range(len(list1)):
    x=dectohex(int(list1[i]))
    list2.append(x)
list1.clear()
for j in list2:
    sum=0
    for k in j:
        sum+=int(k)
    list1.append(sum)
count=0    
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if (i<j and list1[i] > list1[j]):
            count+=1
print(count)





    


    
    
