n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(n):
  for j in range(n):
    if li[i]<li[j]:
      c+=1
print(c)
