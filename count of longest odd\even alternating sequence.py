s=list(input())
def ch(x):
  if int(i)%2==0:
    return "e"
  else:
    return "o"
li=[]
for i in s:
  li.append(ch(i))
c=1
lis=[]
for i in range(len(li)-1):
  if li[i]=="e" and li[i+1]=="o" or li[i]=="o" and li[i+1]=="e":
    c+=1
  else:
    lis.append(c)
    c=1
lis.append(c)
m=max(lis)
if m==1:
  print(0)
else:
  print(m)
