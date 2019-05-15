#include <iostream>
#include<cstdlib>

int main() {
  int n,k,arr[20];
  std::cin>>n>>k;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=n-k;i<n;i++){
    std::cout<<arr[i]<<" ";
  }
}
