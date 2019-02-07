n=int(input())
li=list(map(int,input().split()))
s=0
lis=[]
for i in range(len(li)):
  s+=li[i]
  lis.append(s)
print(*lis[::-1])
