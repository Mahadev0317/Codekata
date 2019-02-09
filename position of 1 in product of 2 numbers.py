n,k=map(int,input().split())
s=bin(n*k)[2:]
s=s[::-1]
for i in range(len(s)):
  if s[i]=="1":
    print(i+1)
    break
