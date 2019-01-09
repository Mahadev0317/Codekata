n,a,d=map(int,input().split())
s=a
for i in range(1,n):
  s=s+((d*i)+a)
print(s)
