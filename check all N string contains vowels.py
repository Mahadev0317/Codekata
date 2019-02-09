v=["a","e","i","o","u"]
li=[]
for i in range(int(input())):
  s=input()
  for j in s:
    if j in v:
      li.append(True)
      break
  else:
      li.append(False)
if all(li):
  print("yes")
else:
  print("no")
