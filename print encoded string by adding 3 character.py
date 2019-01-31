def check(x):
  if ord(x) in range(97,120) or ord (x) in range(65,88):
    return chr(ord(x)+3)
  else:
    if x=="x":
      return "a"
    elif x=="X":
      return "A"
    elif x=="y":
      return "b"
    elif x=="Y":
      return "B"
    elif x=="z":
      return "c"
    elif x=="Z":
      return "C"
st=input()
s=''
for i in st:
  s+=check(i)
print(s)
