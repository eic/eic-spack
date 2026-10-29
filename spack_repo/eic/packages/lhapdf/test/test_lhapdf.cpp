// Stand-alone test for the lhapdf package: link against libLHAPDF and print
// the library version. No PDF sets are needed.
#include "LHAPDF/LHAPDF.h"

#include <iostream>

int main() {
  std::cout << "LHAPDF version: " << LHAPDF::version() << std::endl;
  return 0;
}
