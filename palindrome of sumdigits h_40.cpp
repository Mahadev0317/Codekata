#include <iostream>

int palindrome(int x){
  int y=0,k=0;
  while(x>0){
    y=x%10;
    k=(k*10)+y;
    x=x/10;
  }
  return k;
}

int main() {
  int n,r=0,c=0;
  std::cin>>n;
  while(n>0){
    r+=n%10;
    n=n/10;
  }
  c=palindrome(r);
  if(c==r){
    std::cout<<"YES";}
  else
    std::cout<<"NO";
}
