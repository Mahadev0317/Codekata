def catalan(n):
  if n<=1:
    return 1
  else:
    r=0
    for i in range(n):
      r+=catalan(i)*catalan(n-i-1)
    return r
li=[]
for i in range(int(input())+1):
  li.append(catalan(i))
print(*li)
