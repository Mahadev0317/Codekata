s=list(map(str,input().split(" ")))
for i in range(0,len(s)):
  if (i==0):
    print(s[i][::-1],end=" ")
  elif(i==len(s)-1):
    st=s[i][:-1]
    if (i%2==0):
      print(st[::-1],end=" ")
    else:
      print(st,end=" ")
  else:
    print(s[i],end=" ")
