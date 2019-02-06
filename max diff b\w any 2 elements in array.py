n=int(input())
lis=sorted(list(map(int,input().split())))
print(lis[n-1]-lis[0])
