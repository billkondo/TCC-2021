#ifndef MORRIS_PLUS_H
#define MORRIS_PLUS_H

#include <vector>
#include "morris.hpp"

struct MorrisPlus {
  int T;
  std::vector<Morris> morris;

  MorrisPlus(int T);

  void adiciona();
  int conta();
};

#endif