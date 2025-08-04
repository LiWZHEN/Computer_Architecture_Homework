#include "hello.h"
#include <iostream>

extern "C" {
  void Hello() {
    std::cout << "Hello World!\n";
  }
  int plus(int a, int b) {
    return a + b;
  }
}