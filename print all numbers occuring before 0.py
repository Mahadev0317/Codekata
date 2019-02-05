input()
n=input()
s=""
k=0
for i in range(1,len(n)):
  if n[i]=="0":
    s=s+n[k:i]
    k=i+1
for i in range(len(s)-1):
  print(s[i],end=" ")
print(s[len(s)-1])
