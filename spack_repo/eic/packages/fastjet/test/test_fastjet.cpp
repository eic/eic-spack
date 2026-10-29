// Stand-alone test for the fastjet package, after the FastJet short example:
// anti-kt with R = 0.7 merges the first two particles into one jet.
#include "fastjet/ClusterSequence.hh"

#include <cstdio>
#include <vector>

int main() {
  std::vector<fastjet::PseudoJet> particles = {
      {99.0, 0.1, 0, 100.0}, {4.0, -0.1, 0, 5.0}, {-99.0, 0, 0, 99.0}};
  fastjet::JetDefinition jet_def(fastjet::antikt_algorithm, 0.7);
  fastjet::ClusterSequence cs(particles, jet_def);
  std::vector<fastjet::PseudoJet> jets = fastjet::sorted_by_pt(cs.inclusive_jets());
  std::printf("jets: %zu\n", jets.size());
  for (std::size_t i = 0; i < jets.size(); ++i) {
    std::printf("jet %zu: pt %g\n", i, jets[i].pt());
  }
  return jets.size() == 2 ? 0 : 1;
}
