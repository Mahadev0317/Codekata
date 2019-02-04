n=int(input())
l=[]
for i in range(n):
  a=input()
  l.append(a)
m=len(min(l,key=len))
s=''
f=0
for i in range(m):
  for j in range(len(l)-1):
    if l[j][i]==l[j+1][i]:
      continue
    else:
      print(s)
      f=1
  else:
    s=s+l[j][i]
  if f==1:
    break
else:
  print(s)
