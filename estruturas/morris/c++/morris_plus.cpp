#include "morris_plus.hpp"
#include <cstdlib>
#include <cmath>

MorrisPlus::MorrisPlus(int T) : T(T) {
  morris.resize(T, Morris());
}

void MorrisPlus::adiciona() {
  for (int i = 0; i < T; ++i)
    morris[i].adiciona();
}

int MorrisPlus::conta() {
  double sum = 0;
  for (int i = 0; i < T; ++i)
    sum += morris[i].conta();
  
  return floor(sum / T);
}