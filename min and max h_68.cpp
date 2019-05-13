#include <iostream>
#include<string.h>

int main() {
  int n,arr[20],min,max,x=0,y=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
    if(i==0){
      min=arr[0];
      max=arr[0];}
    if(min>arr[i]){
      min=arr[i];
      x=i;}
    if(max<arr[i]){
      max=arr[i];
      y=i;}
  }
  std::cout<<x+1<<" "<<y+1;
}
