#include <iostream>

int max(int *arr,int x,int n)
{
  int m=arr[x];
  for(int i=x;i<n;i++)
  {
    if (arr[i]>m)
    m=arr[i];
  }
  return m;
}
int main() {
  int n;
  std::cin>>n;
  int a[20];
  for(int i=0;i<n;i++)
  {
    std::cin>>a[i];
  }
  for(int j=0;j<n;j++)
  {
    if (j==n-1)
    a[j]=0;
    else
    a[j]=max(a,j+1,n);
  }
  for(int k=0;k<n;k++)
  {
    std::cout<<a[k]<<" ";
  }
}
