n=int(input())
li=[]
for i in range(n):
  lis=list(map(int,input().split()))
  li.append(lis)
a=0;b=0
k=n-1
for i in range(n):
  a+=li[i][i]
  b+=li[i][k]
  k-=1
print(a*b)
