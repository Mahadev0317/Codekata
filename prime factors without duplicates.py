x=int(input())
lis=[]
def primefactors(x):
  while x%2==0:
    lis.append(2)
    x=x/2
  for i in range(3,int(pow(x,(1/2))+1),2):
    while x%i==0:
      lis.append(i)
      x=x/i
  if x>2:
    lis.append(int(x))
primefactors(x)
print(*set(lis))
