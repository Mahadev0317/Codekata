li=list(input())
lis=[]
for i in li:
  if i in lis:
    print("yes")
    break
  else:
    lis.append(i)
else:
  print("no")
