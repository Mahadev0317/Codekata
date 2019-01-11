n=input()
a=0
d=0
for i in n:
  if i.isdigit():
    d+=1
  elif i.isalpha():
    a+=1
if a>0 and d>0:
  print("Yes")
else:
  print("No")
