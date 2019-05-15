#include <iostream>
#include<vector>
#include <bits/stdc++.h> 
#include <boost/algorithm/string.hpp>

int main() {
  std::string s;
  getline(std::cin,s);
  std::vector<std::string> op;
  boost::split(op, s, boost::is_any_of(" "));
  std::cout<<op[1]<<" "<<op[0];
}
