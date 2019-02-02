s1=input()
s=''
for i in s1:
  if i.isupper():
    s+=i.lower()
  else:
    s+=i.upper()
print(s)
