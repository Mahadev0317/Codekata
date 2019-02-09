n,k=map(int,input().split())
l=list(map(int,input().split()))
li=l[:k]
lis=l[k:]
op=[]
op.extend(sorted(li))
op.extend(sorted(lis,reverse=True))
print(*op)
