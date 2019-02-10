n=int(input())
d={}
v=["a","e","i","o","u","A","E","I","O","U"]
for i in range(n):
  s=input()
  c=0
  for i in s:
    if i in v:
      c+=1
  d[s]=c
for i in (sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)):
  print(i[0])
