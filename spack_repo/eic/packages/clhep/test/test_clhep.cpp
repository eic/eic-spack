// Stand-alone test for the clhep package: build a CLHEP::Hep3Vector from a
// Pythagorean quadruple and check its magnitude, sqrt(3^2 + 4^2 + 12^2) = 13.
#include "CLHEP/Vector/ThreeVector.h"

#include <cmath>
#include <iostream>

int main() {
  CLHEP::Hep3Vector v(3., 4., 12.);
  std::cout << "magnitude: " << v.mag() << std::endl;
  return std::abs(v.mag() - 13.) < 1e-12 ? 0 : 1;
}
