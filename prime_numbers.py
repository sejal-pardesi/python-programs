#Prime numbers upto n number
#time complexity = O(n²)
n=int(input("Enter a number = "))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")
            
