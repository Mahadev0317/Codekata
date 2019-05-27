n=int(input())
lis=list(map(int,input().split()))
temp=[];f=0
for i in range(n):
   if f==0:
      temp.append(max(lis))
      k=lis.index(max(lis))
      lis.pop(k)
      f=1
   elif f==1:
      temp.append(min(lis))
      j=lis.index(min(lis))
      lis.pop(j)
      f=0
print(*temp)
