n,k=map(int,input().split())
def prime(x):
  for i in range(2,x):
    if x%i==0:
      return False
      break
  else:
    return True
op=0
for i in range(n,k+1):
  c=0
  s=bin(i)[2:]
  for j in s:
    if j=="1":
      c+=1
  if c>1:
    if prime(c):
      op+=1
print(op)
