n=int(input())
li=list(map(int,input().split()))
s=0
for i in li:
  if i<0:
    s+=i
print(s)
