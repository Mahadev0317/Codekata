s=input()
m=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        k=s[i:j]
        if k==k[::-1]:
            if len(k)>m:
                m=len(k)
print(m)
