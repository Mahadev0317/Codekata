#include <iostream>

int main() {
  int n,arr[20];
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if(i==n-1){
      std::cout<<-1<<" ";
    }
    else if(arr[i+1]<arr[i]){
      std::cout<<arr[i+1]<<" ";
    }
    else{
      std::cout<<-1<<" ";
    }
  }
}
