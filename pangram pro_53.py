st=list(input())
s=[]
for i in st:
  if i!=" " and i not in s:
    s.append(i.lower())
if len(s)==26:
  print("yes")
else:
  print("no")
