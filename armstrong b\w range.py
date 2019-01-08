n,q=map(int,input().split())
def armstrong(n):
  li=list(n)
  l=len(li)
  sum=0
  for i in range(len(li)):
    sum+=(int(li[i])**l)
  if sum==int(n):
    return True
  else:
    return False
lis=[]
for i in range(n+1,q):
  if armstrong(str(i)):
    lis.append(i)
for i in range(len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
