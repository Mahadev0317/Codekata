#include <iostream>

int main() {
  int n,k,arr[20],m,x=0,op[20],c=0;
  std::cin>>n>>k;
  for(int i=0;i<n;i++)
  {
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if(arr[i]!=k)
    {
      op[x]=arr[i];
      x++;
    }
    else
      c++;
    }
  for(int i=0;i<n-c;i++){
      std::cout<<op[i]<<" ";
  }
}
