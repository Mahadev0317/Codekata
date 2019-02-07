d,m,y=map(int,input().split("/"))
if d in range (1,32) and m in range(1,13) and y in range(1,2100):
  print("yes")
else:
  print("no")
