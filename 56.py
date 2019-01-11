n=input()
def alpha(x):
  return x.isalpha()
def digit(x):
  return x.isdigit()
a=0
d=0
for i in n:
  if digit(i):
    d+=1
  elif alpha(i):
    
