n=int(input())
li=list(map(int,input().split()))
r=li[0]
d=0
for i in range(n-1):
  r=r^li[i+1]
  d+=r
print(d)
