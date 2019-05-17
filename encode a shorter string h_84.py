s=list(input())
c=1
for i in range(len(s)-1):
  if(s[i]==s[i+1]):
    st=s[i]
    c+=1
  else:
    if c>1:
      print(str(c)+"*"+st,end="")
    else:
      print(s[i],end="")
    st=""
    c=1
if c>1:
  print(str(c)+"*"+st,end="")
else:
  print(s[-1],end="")
