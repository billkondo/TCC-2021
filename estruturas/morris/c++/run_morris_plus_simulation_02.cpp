#include <map>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <fstream>
#include <iostream>

#include "morris_plus.hpp"
#include "../../modules/json.hpp"

#define T 1000
#define TAMANHO_DO_CONJUNTO 1000000
#define NUMERO_EXPERIMENTOS 100

using Json = nlohmann::json;

int main() {
  printf("Morris Plus Experimento 02\n");
  srand(0);

  std::map<int, int> frequencies;
  for (int j = 1; j <= NUMERO_EXPERIMENTOS; ++j) {
    MorrisPlus morris_plus = MorrisPlus(T);
    for (int i = 1; i <= TAMANHO_DO_CONJUNTO; ++i) {
      morris_plus.adiciona();
      if (i % 100000 == 0) printf("%d: %d\n", j, i);
    }

    if (j % 50 == 0)
      printf("%d / %d\n", j, NUMERO_EXPERIMENTOS);

    int y = morris_plus.conta();
    if (frequencies.find(y) == frequencies.end()) 
      frequencies[y] = 1;
    else 
      frequencies[y] += 1;
  }

  Json json;
  for (auto f: frequencies) json[std::to_string(f.first)] = f.second;

  std::ofstream json_file("../morris_plus_simulation_02_result.json");
  json_file << json << std::endl;

  return 0;
}