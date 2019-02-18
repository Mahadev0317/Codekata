s=list(input())
a=list("dhoni")
for i in s:
    if i not in a:
        print("no")
        break
else:
    print("yes")
