n=list(input())
s=""
for i in n:
  if i.isupper():
    s+=i.lower()
  else:
    s+=i.upper()
print(s)
