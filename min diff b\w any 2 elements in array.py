n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in li:
  if i not in lis:
    lis.append(i)
lis=sorted(lis)
print(lis[1]-lis[0])
