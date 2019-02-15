n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
  b=bin(i)[2:]
  c=0
  for j in b:
    if j=="1":
      c+=1
  d[i]=c
for i in sorted(d.items(), key=lambda kv: (kv[1],kv[0]), reverse=True):
  print(i[0])
