st=list(input())
s1=''
s2=''
for i in range(0,len(st),2):
  s1=s1+st[i]
for i in range(1,len(st),2):
  s2=s2+st[i]
print(s1,s2)
