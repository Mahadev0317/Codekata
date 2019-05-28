n,s=map(int,input().split())
l=sorted(list(map(int,input().split())),reverse=True)
c=0
for i in range(n):
   c+=s//l[i]
   s=s%l[i]
print(c)
