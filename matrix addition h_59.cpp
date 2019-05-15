#include <iostream>
#include<cstdlib>

int main() {
  int n,k,arr[20],arr2[20],sum[20];
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int j=0;j<n;j++){
    std::cin>>arr2[j];
  }
  for(int i=0;i<n;i++){
    sum[i]=arr[i]+arr2[i];
  }
  for(int i=0;i<n;i++){
    std::cout<<sum[i]<<" ";
  }
}
