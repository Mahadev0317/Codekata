n=int(input())
li=list(map(int,input().split()))
lis=sorted(li)
for i in range(n):
    if li[i]!=lis[i]:
        print(i)
        break
