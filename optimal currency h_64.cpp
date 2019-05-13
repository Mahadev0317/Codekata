#include <iostream>

int main() {
  int n,c=0;
  std::cin>>n;
  int arr[10]={1000,500,100,50,10,1};
  for(int i=0;i<6;i++)
  {
    c+=n/arr[i];
    n=n%arr[i];
  }
  std::cout<<c;
}
