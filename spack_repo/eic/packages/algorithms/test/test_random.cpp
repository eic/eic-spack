#include <algorithms/logger.h>
#include <algorithms/random.h>

#include <cstdlib>
#include <iostream>

int main() {
  auto& serviceSvc = algorithms::ServiceSvc::instance();
  auto& randomSvc  = algorithms::RandomSvc::instance();
  randomSvc.setProperty("seed", std::size_t{42});
  serviceSvc.init();
  if (!serviceSvc.ready()) {
    std::cerr << "services not ready" << std::endl;
    return EXIT_FAILURE;
  }
  const auto generator = randomSvc.generator();
  double sum           = 0;
  for (int i = 0; i < 10000; ++i) {
    const double x = generator.uniform_double(2.0, 3.0);
    if (x < 2.0 || x >= 3.0) {
      std::cerr << "uniform_double out of range: " << x << std::endl;
      return EXIT_FAILURE;
    }
    sum += x;
  }
  const double mean = sum / 10000;
  std::cout << "algorithms::RandomSvc mean: " << mean << std::endl;
  return (mean > 2.45 && mean < 2.55) ? EXIT_SUCCESS : EXIT_FAILURE;
}
