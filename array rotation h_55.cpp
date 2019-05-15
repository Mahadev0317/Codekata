#include <iostream>

int main() {
  int n,d,arr[20],j=0,temp[20],k=0,l=0;
  std::cin>>n>>d;
  for(int i=0;i<n;i++){
    if(i<d){
      std::cin>>temp[k];
      k++;
    }
    else{
      std::cin>>arr[l];
      l++;
    }
  }
  for(int i=0;i<k;i++){
    arr[l]=temp[i];
    l++;
  }  
  for(int i=0;i<l;i++){
    std::cout<<arr[i]<<" ";
  }
}
