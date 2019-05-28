n=int(input())
def prime(x):
   for i in range(2,x):
      if x%i==0:
         return False
   else:
      return True
c=0
for i in range(2,n):
   if prime(i) is True and str(i)[-1]=="3":
      c+=i
print(c)
