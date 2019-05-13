#include <iostream>
#include<string.h>

int main() {
  int a=0,b=0,x,y,d,com=0,k=0;
  std::string st=".com";
  std::string s;
  std::cin>>s;
  for(int i=0;i<s.size();i++){
    if(s[i]=='@'){
      a++;
      x=i;}
    if(s[i]=='.'){
      b++;
      y=i;}
  }
  for(int i=s.size()-4;i<s.size();i++){
    if(s[i]==st[k]){
      k++;
      continue;}
    else{
      com=1;}
  }
  d=y-x;
  if(a==1 and b==1 and d>3 and x>2 and com==0){
    std::cout<<"YES";}
  else{
    std::cout<<"NO";}
}
