import re
s=input()
r=re.sub(' +', ' ',s)
print(r.strip())
#
