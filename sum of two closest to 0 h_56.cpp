#include <iostream>
#include<cstdlib>
int main() {
  int n,arr[20],min=0,x=0,y=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if(i==0){
      min=abs(abs(arr[i])-abs(arr[i+1]));
    }
    for(int j=i+1;j<n;j++){
      if(abs(abs(arr[i])-abs(arr[j]))<=min){
        min=abs(abs(arr[i])-abs(arr[j]));
        x=i;y=j;
      }
    }
  }
  std::cout<<arr[x]<<" "<<arr[y];
}
