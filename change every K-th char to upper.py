s,k=input().split()
s=list(s)
lis=[]
op=""
for i in range(int(k)-1,len(s),int(k)):
  lis.append(i)
for i in range(len(s)):
  if i in lis:
    op+=s[i].upper()
  else:
    op+=s[i]
print(op)
