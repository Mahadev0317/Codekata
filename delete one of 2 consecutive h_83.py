s=list(input())
m=0
for i in range(len(s)-1):
  if (s[i]==s[i+1]) and m<i+1:
    m=i+1
s.pop(m)
print("".join(s))
