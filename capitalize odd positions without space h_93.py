n=input()
temp=""
f=0
for i in range(len(n)):
  if n[i]==" ":
    temp+=n[i]
  elif f==0:
    temp+=n[i].upper()
    f=1
  elif f==1:
    temp+=n[i]
    f=0

print(temp)
