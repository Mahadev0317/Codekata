n=int(input())
li=list(map(int,input().split()))
m=max(li)
f=0;a=0;b=0
for i in range(0,n-1):
  for j in range(i+1,n):
    if (li[i]+li[j])==0:
      print(li[i],li[j])
      break
      f=1
    else:
      if abs(li[i]+li[j])<m:
        m=li[i]+li[j]
        a=i
        b=j
  if f==1:
    break
else:
  print(li[a],li[b])
