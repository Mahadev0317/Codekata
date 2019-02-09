n,k=map(int,input().split())
li=list(map(int,input().split()))
def binarysearch(arr,l,r,x):
  if r>=l:
    m=l+(r-l)//2
    if arr[m]==x:
      print("yes")
    elif arr[m]<k:
      return binarysearch(arr,m+1,r,k)
    else:
      return binarysearch(arr,l,m-1,k)
  else:
    print("no")
binarysearch(li,0,n-1,k)
