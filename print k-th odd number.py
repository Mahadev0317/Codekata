n,k=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in li:
    if i%2!=0:
        lis.append(i)
print(lis[k-1])
