#include <iostream>

int check(int *arr,int x,int n){
  int f=0;
  for(int i=0;i<n;i++){
    if(n*x==arr[i]){
      f=1;
      return true;
      break;
    }
  }
  if(f==0){
    return false;
  }
  return 0;
}

int main() {
  int n,arr[20],c=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    std::cin>>arr[i];
  }
  for(int i=0;i<n;i++){
    if (check(arr,i+1,n)==true){
      c++;
    }
  }
  std::cout<<c;
}
