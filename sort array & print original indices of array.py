n=int(input())
li=list(map(int,input().split()))
lis=sorted(li)
op=[]
for i in lis:
  op.append(li.index(i)+1)
print(*op)
