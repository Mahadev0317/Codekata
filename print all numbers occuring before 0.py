input()
n=input()
s=""
k=0
for i in range(1,len(n)):
  if n[i]=="0":
    s=s+n[k:i]
    k=i+1
print(*list(s))
