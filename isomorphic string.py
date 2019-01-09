s1,s2=input().split()
def check(s):
  c=0
  for i in range(len(s1)-1):
    if s[i]!=s[i+1]:
      c+=1
  return c
if check(s1)==check(s2):
  print("yes")
else:
  print("no")
