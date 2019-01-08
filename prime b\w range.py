n,q=map(int,(input().split()))
def prime(p):
  if p>1:
    for i in range(2,p):
      if p%i==0:
        return False
    else:
      return True
lis=[]
for j in range(n+1,q):
  if prime(j):
    lis.append(j)
for i in range(len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
