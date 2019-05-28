n=int(input())
lis=list(map(int,input().split()))
d={}
for i in lis:
   if i not in d:
      d[i]=1
   elif i in d:
      d[i]+=1
m=0
for k,v in d.items():
   if v>m:
      op=k
      m=v
print(op)
