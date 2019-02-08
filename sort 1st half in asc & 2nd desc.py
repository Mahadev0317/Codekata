n=int(input())
l=list(map(int,input().split()))
li=l[:n//2]
lis=l[n//2:]
op=[]
op.extend(sorted(li))
op.extend(sorted(lis,reverse=True))
print(*op)
