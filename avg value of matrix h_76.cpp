#include <iostream>
#include<iomanip>
int main() {
  int n,arr[20][20],sum=0;
  float op=0;
  std::cin>>n;
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      std::cin>>arr[i][j];
    }
  }
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      sum+=arr[i][j];
    }
  }
  op=float(sum)/float((n*n));
  std::cout<<std::fixed<<std::setprecision(6)<<op;
}
