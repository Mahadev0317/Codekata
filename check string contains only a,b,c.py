s=input()
c=0
for i in s:
  if i!="a" and i!="b" and i!="c":
    c+=1
if c<=1:
  print("yes")
else:
  print("no")
