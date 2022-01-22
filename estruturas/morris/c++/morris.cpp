#include "morris.hpp"
#include <cstdlib>

Morris::Morris() {
  X = 0;
}

void Morris::adiciona() {
  int r = rand() % (1 << X);
  if (r == 0) X++;
}

int Morris::conta() {
  return (1 << X) - 1;
}