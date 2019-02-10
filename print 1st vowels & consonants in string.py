s=input()
li=["a","e","i","o","u"]
v=""
c=""
for i in s:
  if i in li:
    v+=i
  else:
    c+=i
print(v+c)
