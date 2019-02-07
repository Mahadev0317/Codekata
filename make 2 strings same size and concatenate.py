n,k=input().split()
s=''
if len(n)!=len(k):
  d=min(len(n),len(k))
  s=n[:d]+k[:d]
else:
  s=n+k
print(s)
