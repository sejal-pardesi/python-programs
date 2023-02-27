#find number of digits in a number
#time complexity = O(logn)
n=int(input("Enter a number = "))
c=0
while(n!=0):
    n=n//10
    c=c+1
print(c)

#efficient code 
#time complexity = O(1)
import math
n=int(input("Enter a number = "))
k=math.log(n,10) #where 10 is the base
print(math.floor(k+1))