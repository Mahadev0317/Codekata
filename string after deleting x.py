li=list(input().split())
s=input()
lis=[]
for i in li:
  if i!=s:
    lis.append(i)
print(*lis)
