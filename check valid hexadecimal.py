n=input()
try :
  int(n,16)
  print("yes")
except ValueError:
  print("no")
