li=list(input())
def ch(x):
  if li!=li[::-1]:
    return True
i=0
while i<len(li):
  if ch(li):
    print("".join(li))
    break
  else:
    li.pop()
  i+=1
