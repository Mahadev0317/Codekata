n=list(input())
lis=[]
for i in n:
  if i.isdigit():
    lis.append(True)
  else:
    lis.append(False)
if all(lis)==True:
  print("yes")
else:
  print("no")
