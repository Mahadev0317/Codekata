n=int(input())
li=list(map(int,input().split()))
lis=[0]*10
for i in range(len(li)):
  lis[li[i]]+=1
op=[]
for i in range(len(lis)):
  if lis[i]==1:
    print(i)
