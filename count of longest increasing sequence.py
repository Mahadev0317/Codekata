n=int(input())
li=list(map(int,input().split()))
c=1
f=0
lis=[]
for i in range(len(li)-1):
  if li[i]<li[i+1]:
    if f==0:
      c+=1
      f=1
    else:
      c+=1
  else:
    lis.append(c)
    c=1
    f=0
lis.append(c)
print(max(lis))
