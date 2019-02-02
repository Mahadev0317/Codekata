s=input()
a=0;b=0
for i in s:
  if i=="(":
    a+=1
  else:
    b+=1
if a==b:
  print("yes")
else:
  print("no")
