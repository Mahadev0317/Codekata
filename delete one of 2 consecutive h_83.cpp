#include <iostream>
#include<string>

using namespace std;
int main() {
  string s;
  int max=0;
  cin>>s;
  for (int i=0;i<s.length()-1;i++){
    if(s[i]==s[i+1] and max<i+1){
      max=i+1;
    }
  }
  for(int i=0;i<s.length();i++){
    if(i!=max){
      cout<<s[i];
    }
  }
}
