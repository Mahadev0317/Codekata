n=int(input())
lis=list(map(str,input().split()))
lis=[i.lower() for i in lis]
lis=sorted(lis)
for i in range(len(lis)):
    print(lis[i])
