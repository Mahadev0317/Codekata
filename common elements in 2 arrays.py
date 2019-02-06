n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
lis=[]
for i in range(0,n):
  for j in range(0,len(k)):
    if l[i]==k[j]:
      lis.append(l[i])
      k.pop(j)
      break
print(*lis)
