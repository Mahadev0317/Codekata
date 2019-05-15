#include <iostream>

int main() {
  std::string s,arr[20];
  int f=0,k=0;
  getline(std::cin,s);
  for(int i=0;i<s.size();i++){
    if(s[i]==' '){
      f=1;k=i;
      continue;
    }
    if(f==1){
      std::cout<<s[i];
    }
  }
  std::cout<<" ";
  for(int i=0;i<k;i++){
    std::cout<<s[i];
  }
}
