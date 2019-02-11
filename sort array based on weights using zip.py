n=int(input())
li=list(map(int,input().split()))
lis=list(map(int,input().split()))
d={}
op=[i for _,i in sorted(zip(lis,li))]
print(*op)
