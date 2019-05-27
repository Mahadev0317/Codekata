lis=list(map(str,input().split()))
for i in lis:
   if not i[0].isupper():
      print("no")
      break
else:
   print("yes")
