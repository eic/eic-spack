R__LOAD_LIBRARY(libedm4eicDict)

#include "edm4eic/ReconstructedParticleCollection.h"

#include <iostream>

void test_edm4eic() {
  edm4eic::ReconstructedParticleCollection particles;
  auto particle = particles.create();
  particle.setEnergy(1.5);
  std::cout << "particles: " << particles.size() << ", energy: " << particles[0].getEnergy()
            << std::endl;
}
