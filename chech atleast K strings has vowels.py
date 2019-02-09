v=["a","e","i","o","u"]
n,k=map(int,input().split())
c=0
for i in range(n):
  s=input()
  for j in s:
    if j in v:
      c+=1
      break
if c>=k:
  print("yes")
else:
  print("no")
