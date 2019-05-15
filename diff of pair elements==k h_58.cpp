#include <iostream>
#include<cstdlib>

int diff(int x,int y){
  return(abs(abs(x)-abs(y)));
}
int main() {
  int n,k,arr[20],c=0;
  std::cin>>n>>k;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      if(diff(arr[i],arr[j])==k){
        c++;
      }
    }
  }
  std::cout<<c;
}
