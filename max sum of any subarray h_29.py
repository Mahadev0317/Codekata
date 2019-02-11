n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in li:
  if i<0:
    lis.append(False)
  else:
    lis.append(True)
c=0
for i in li:
  c+=i
if all(lis):
  print(c)
elif max(li)<c:
  print(c)
else:
  print(max(li))
