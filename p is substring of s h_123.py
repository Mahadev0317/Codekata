s,p=map(str,input().split())
for i in range(len(s)-len(p)):
   if s[i:i+len(p)]==p:
      print("yes")
      break
else:
   print("no")
