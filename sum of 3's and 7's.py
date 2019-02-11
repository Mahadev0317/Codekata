n=int(input())
li=[0,1,2,3,4,5,8,11,16,28,47]
if n%3==0 or n%7==0 or n%10==0 or n not in li:
  print("yes")
else:
  print("no")
