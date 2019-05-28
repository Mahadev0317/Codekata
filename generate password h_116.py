a,b=input().split()
temp=""
def string(n):
   x=""
   for i in range(1,n+1):
      x+=str(i)
   return x
if len(b)>len(a):
   a+=string(len(b)-len(a))
elif len(a)>len(b):
   b+=string(len(a)-len(b))
for i in range(len(a)):
   temp+=(a[i]+b[i])
print(temp)
