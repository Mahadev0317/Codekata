n=int(input())
temp=[];c=0
def prime(x):
   for i in range(2,x):
      if x%i==0:
         return False
   else:
      return True
for i in range(2,1000):
   if prime(i) is True:
      temp.append(i)
for i in range(len(temp)-1):
   for j in range(i+1,len(temp)):
      if(temp[i]+temp[j])==n:
         c+=1
   if(temp[i]+temp[i])==n:
      c+=1
if (temp[-1]+temp[-1])==n:
   c+=1
print(c)
