// Stand-alone test for the vecgeom package: the capacity of a box with
// half-lengths 1, 2 and 3 is 2 * 4 * 6 = 48.
#include "VecGeom/volumes/UnplacedBox.h"

#include <cmath>
#include <iostream>

int main() {
  vecgeom::UnplacedBox box(1., 2., 3.);
  const double capacity = box.Capacity();
  std::cout << "box capacity: " << capacity << std::endl;
  return std::abs(capacity - 48.) < 1e-9 ? 0 : 1;
}
