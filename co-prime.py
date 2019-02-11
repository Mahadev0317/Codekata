n,k=input().split()
n=len(n)
k=len(k)
li=[]
def factors(x):
  for i in range(2,x+1):
    if x%i==0:
      li.append(i)
factors(k);factors(n)
lis=[]
for i in li:
  if i in lis:
    print("no")
    break
  else:
    lis.append(i)
else:
  print("yes")
