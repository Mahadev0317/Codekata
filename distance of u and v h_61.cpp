#include <iostream>

int abs(int x, int y){
  if(x>y)
    return x-y;
  else
    return y-x;
}
int main() {
  int n,arr[20],u,v,a[20],b[20],w=0,y=0,m[20],k=0,min;
  std::cin>>n;
  for(int i=0;i<n;i++)
    std::cin>>arr[i];
  std::cin>>u>>v;
  for(int i=0;i<n;i++)
  {
    if(arr[i]==u)
    {  a[w]=i;
      w++;}
    else if(arr[i]==v)
    { b[y]=i;
      y++; }
  }
  for(int i=0;i<w;i++)
  {
    for(int j=0;j<y;j++)
    {
      m[k]=abs(a[i],b[j]);
      k++;
    }}
  for(int i=0;i<k;i++)
    if (i==0)
      min=m[0];
    else if(m[i]<min)
      min=m[i];
  std::cout<<min;
}
