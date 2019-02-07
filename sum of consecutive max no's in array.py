n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in range(len(li)-1):
  lis.append(max(li[i],li[i+1]))
print(sum(lis))
