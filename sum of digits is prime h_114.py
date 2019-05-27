l,r=map(int,input().split())
def func(x):
   s=0
   while x>0:
      r=x%10
      s+=r
      x=x//10
   if s>1:
      for i in range(2,s):
         if s%i==0:
            f=1
            return False
            break
      else:
         return True
   else:
      return False
c=0
for i in range(l,r):
   if func(i) is True:
      c+=1
print(c)
