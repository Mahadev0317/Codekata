#include <iostream>

int main() {
  int a,b,c=0;
  std::cin>>a>>b;
  while(a>=b){
    a-=b;
    c++;
  }
  std::cout<<c;
}
