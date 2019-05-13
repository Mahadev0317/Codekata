#include <iostream>

int main() {
  int n,arr[20],max,min;
  std::cin>>n;
  for(int i=0;i<n;i++)
  {
    std::cin>>arr[i];
    if(i==0)
    {
    min=arr[0];
    max=arr[0];
    }
    else{
    if(arr[i]<min)
    min=arr[i];
    else if(arr[i]>max)
    max=arr[i];
    }
  }
  std::cout<<max-min;
}
