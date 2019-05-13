#include <iostream>
#include<string.h>
int check(std::string x,int l,std::string y) {
  int flag=0;
  for(int i=0;i<l;i++){
    if (x[i]==y[i])
      continue;
    else
      flag=1;
      return false;
      break;
    }
  if(flag==0)
    return true;
}
int main() {
  int n,c=0;
  std::string arr[20],s;
  std::cin>>n;
  for(int i=0;i<n;i++)
    std::cin>>arr[i];
  std::cin>>s;
  int len= s.size();
  for(int i=0;i<n;i++){
    if(check(arr[i],len,s)==true)
      c++;
    }
  std::cout<<c;
}
