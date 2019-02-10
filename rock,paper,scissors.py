a,b=input().split()
if a==b:
  print("D")
elif a=="R" and b=="P" or a=="P" and b=="R":
  print("P")
elif a=="P" and b=="S" or a=="S" and b=="P":
  print("S")
elif a=="R" and b=="S" or b=="R" and a=="S":
  print("R")
