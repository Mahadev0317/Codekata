s=input()
li=[]
li.append(s[0])
for i in range(1,len(s)):
  if s[i] in li:
    print("No")
    break
  else:
    li.append(s[i])
else:
  print("Yes")
