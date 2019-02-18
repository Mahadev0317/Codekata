s=input()
a=s[0]
for i in range(1,len(s)):
    if ord(a)<ord(s[i]):
        print(s[i:])
        break
else:
    print(s)
