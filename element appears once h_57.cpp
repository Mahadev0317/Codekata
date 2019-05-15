#include <iostream>
#include<cstdlib>

int not_in(int *arr,int x,int y,int n){
  int f=0;
  for(int i=0;i<n;i++){
    if(i!=y and x==arr[i]){
      f=1;
      return false;
      break;
    }
  }
  if(f==0){ return true;}
  return 0;
}
int main() {
  int n,arr[20];
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if(not_in(arr,arr[i],i,n)==true){
      std::cout<<arr[i];
    }
  }
}
