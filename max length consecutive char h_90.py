n=input()
temp=dict()
ch=n[0]
le=1
for i in range(1,len(n)):
  if n[i]==ch:
    le+=1
  else:
    if ch in temp and temp[ch]<le:
      temp[ch]=le
    elif ch not in temp:
      temp[ch]=le
    ch=n[i]
    le=1
if ch in temp and temp[ch]<le:
  temp[ch]=le
elif ch not in temp:
  temp[ch]=le
m=0
for k,v in temp.items():
  if v>m:
    m=v
    ch=k
print(ch,m)
