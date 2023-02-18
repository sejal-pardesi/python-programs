#Sum of n natural numbers using an efficient function which takes O(1) constant time
def sum_of_num(n):
  return int(n*(n+1)/2)
num=int(input("Enter a number = "))
print(sum_of_num(num))
