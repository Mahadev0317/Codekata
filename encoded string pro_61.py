s1=input()
s2=input()
op=''
for i in range(len(s2)):
  x=ord(s2[i])-96
  x=x+ord(s1[i])
  if x>ord('z'):
    x=x-ord('z')
    x=x+96
  op+=chr(x)
print(op)
