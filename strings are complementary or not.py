n=input()
m=input()
s=n+m
li=[]
if len(s)==26:
  for i in s:
    if i in li:
      print(i)
      print("non-complementary")
      break
    else:
      li.append(i)
  else:
    print("complementary")
else:
  print("non-complementary")
