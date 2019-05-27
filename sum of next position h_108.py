s=input()
n=0
if len(s)==1:
    n=int(s)*int(s)
else:
    for i in range(len(s)):
        if i==len(s)-1:
            n+=(int(s[i])**int(s[0]))
        else:
            n+=(int(s[i])**int(s[i+1]))
print(n)
