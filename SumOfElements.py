def main(array):
  sum=0
  for i in array:
    sum+=i
  return sum

n=int(input())
arr=[]
#arr=list(map(int,input().split()))
for i in range(n):
  element=int(input())
  arr.append(element)
main(arr)
