l,r=map(int,input().split())
def prime(p):
  if p>1:
    for i in range(2,p):
      if p%i==0:
        return False
    else:
      return True
c=0
for i in range(l,r+1):
  if prime(i):
    c+=1
print(c)
