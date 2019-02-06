n=int(input())
li=list(map(int,input().split()))
even=[]
odd=[]
for i in li:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
if len(even)==1:
  print(*even)
else:
  print(*odd)
