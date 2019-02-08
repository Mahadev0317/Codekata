n=int(input())
s=bin(n)[2:]
s=s[::-1]
for i in range(len(s)):
  if int(s[i])==1:
    print(i+1)
    break
