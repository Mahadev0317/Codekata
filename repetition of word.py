n=list(input().split())
m=input()
c=0
for i in range(len(n)):
  if n[i]==m:
    c+=1
print(c)
