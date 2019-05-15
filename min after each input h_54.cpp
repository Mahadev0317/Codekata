#include <iostream>

int main() {
  int n,arr[20],min=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
    if(i==0){
      min=arr[0];
    }
    if(arr[i]<min){
      min=arr[i];
      std::cout<<min<<" ";
    }
    else{
      std::cout<<min<<" ";
    }
  }
}
