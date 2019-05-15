#include <iostream>
#include<cstdlib>

int main() {
  int n,arr[20],min=0,x=0,y=0,a=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if(i==0){
      min=arr[i]+arr[i+1];
    }
    for(int j=i+1;j<n;j++){
      if (abs(arr[i]+arr[j])<=abs(min)){
        min=arr[i]+arr[j];
        x=i;y=j;
      }  
    }
  }
  std::cout<<arr[x]<<" "<<arr[y];
}
