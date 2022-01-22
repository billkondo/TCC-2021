#include <cstdio>
#include <vector>
#include <iomanip>
#include <fstream>
#include <iostream>

#include "morris_plus.hpp"
#include "../../modules/json.hpp"

#define T 1000
#define TAMANHO_DO_CONJUNTO 1000000

using Json = nlohmann::json;

int main() {
  printf("Morris Plus Experimento 01\n");
  srand(0);

  MorrisPlus morris_plus = MorrisPlus(T);
  std::vector<int>  contadores_devolvidos_por_morris_plus(TAMANHO_DO_CONJUNTO + 1),
                    contadores_esperados(TAMANHO_DO_CONJUNTO + 1);
  std::vector<double> erro_relativo(TAMANHO_DO_CONJUNTO + 1);

  contadores_devolvidos_por_morris_plus[0] = morris_plus.conta();
  contadores_esperados[0] = 0;
  erro_relativo[0] = 0;
  for (int i = 1; i <= TAMANHO_DO_CONJUNTO; ++i) {
    morris_plus.adiciona();
    int contador = morris_plus.conta();

    contadores_devolvidos_por_morris_plus[i] = contador;
    contadores_esperados[i] = i;
    erro_relativo[i] = double(contador - i) / double(i);

    if (i % 100 == 0)
      printf("i = %d\n", i);
  }

  Json json;
  json["contadores_devolvidos_por_morris_plus"] = contadores_devolvidos_por_morris_plus;
  json["contadores_esperados"] = contadores_esperados;
  json["erro_relativo"] = erro_relativo;

  std::ofstream json_file("../morris_plus_simulation_01_result.json");
  json_file << json << std::endl;

  return 0;
}