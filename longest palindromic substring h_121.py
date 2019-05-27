s=input()
temp=""
for i in range(len(s)):
    for j in range(i,len(s)):
        k=s[i:j+1]
        if k==k[::-1] and len(k)>len(temp):
           temp=k
print(temp)
