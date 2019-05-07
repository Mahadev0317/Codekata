m,n=input().split()
for i in range(0,len(m)-1):
  if m[i:i+2] in n:
    print('yes')
    break
else:
  print('no')
