n=int(input())
li=list(map(int,input().split()))
d={}
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
lis=[]
for i in sorted(d.items(),key=lambda kv: (kv[1],kv[0]),reverse=True):
  lis.append(i[0])
print(*lis)
