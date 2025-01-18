#include<iostream>
#include<unordered_map>

//A hash is used to map keys to values. Provides for access, insertion and deletion by hashing the keys.
int main () {

  unordered_map<std::string, int> map;

  map["a"] = 1;
  map["b"] = 2;

  std::cout<<"The vale of A is "<<map["a"]<<std::endl;

  if(map.find("b") != map.end()){
    std::cout<<"The value of B is "<<map["b"]<<std::endl;
  } 
  return 0;
}