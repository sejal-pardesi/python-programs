#Prime numbers upto n number using Sieve of Eratosthenes
def sieveOfEratosthenes(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p=p+1
    for i in range(2,n+1):
        if prime[i]:
            print(i,end=" ")
                

if __name__=='__main__':
    num=int(input("Enter number = "))
    print("Prime numbers upto",num)
    sieveOfEratosthenes(num)
    
#Time Complexity = O(n*log(logn))
