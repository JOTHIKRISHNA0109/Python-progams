def ifprime(n):
  #check the number is prime or not
  for i in range(2,n//2):
    if n%i==0:
      return "No"
      break
  return "Yes"

num=int(input())
print(ifprime(num))
  
