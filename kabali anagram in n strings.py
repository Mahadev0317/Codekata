def check(s):
  s=sorted(s)
  if s[0]=="a" and s[1]=="a":
    if set(list(s))==set(list("kabali")):
      return True
    else:
      return False
  else:
    return False
c=0
for i in range(int(input())):
  if check(input()):
    c+=1
print(c)
