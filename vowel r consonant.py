chr=input()
lis=['a','e','i','o','u']
if chr.isalpha():
  if chr in lis:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
  
