#Check whether a number is Palindrome or not
n=int(input("Enter a number = "))
temp=n
rev=0
while(n!=0):
    a=n%10
    rev=rev*10+a
    n=n//10
if(temp==rev):
    print(temp, "is palindrome")
else:
    print(temp, "is not palindrome")
    
#time complexity =O(d)
#where d is the number of digits
