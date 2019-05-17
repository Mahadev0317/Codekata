s=list(map(str,input().split(" ")))
for i in range(0,len(s)):
  if (i==0):
    print(s[i][::-1],end=" ")
  else:
    print(s[i],end=" ")
