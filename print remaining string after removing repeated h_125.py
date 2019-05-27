s=input()
temp=""
def chk(x,k):
   for j in range(0,len(s)):
      if j!=k and x==s[j]:
         return False
   return True
for i in range(len(s)):
   if chk(s[i],i) is True:
      temp+=s[i]
print(temp)
