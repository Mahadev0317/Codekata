#include <iostream>
#include<cstdlib>

int main() {
  int n,arr[20],arr2[20];
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int j=0;j<n;j++){
    std::cin>>arr2[j];
  }
  for(int i=0;i<n;i++){
    if(arr2[0]==arr[i]){
      std::cout<<i;
    }
  }
}
