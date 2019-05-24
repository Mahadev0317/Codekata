n=input()
temp=""
for i in n:
  if i not in temp:
    temp+=i
print(temp[::-1])
