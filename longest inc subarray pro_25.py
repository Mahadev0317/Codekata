n=int(input())
a=list(map(int,input().split()))
c=1;li=[]
for i in range(n-1):
  if a[i]<a[i+1]:
    c+=1
  else:
    li.append(c)
    c=1
li.append(c)
print(max(li))     
