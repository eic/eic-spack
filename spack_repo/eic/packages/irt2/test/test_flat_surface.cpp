#include <iostream>

#include "FlatSurface.h"

int main() {
  // 100x100 plane at z=10, ray from the origin along +z
  IRT2::FlatSurface plane(TVector3(0, 0, 10), TVector3(1, 0, 0), TVector3(0, 1, 0), 100, 100);
  TVector3 crs;
  bool ok = plane.GetCrossing(TVector3(0, 0, 0), TVector3(0, 0, 1), &crs, false);
  std::cout << "crossing: " << ok << " z=" << crs.z() << std::endl;
  return ok ? 0 : 1;
}
