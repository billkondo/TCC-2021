CXX = g++
CXXFLAGS = -std=c++11

all: run_morris_plus_simulation_01 run_morris_plus_simulation_02

run_morris_plus_simulation_01: run_morris_plus_simulation_01.cpp morris.o morris_plus.o

run_morris_plus_simulation_02: run_morris_plus_simulation_02.cpp morris.o morris_plus.o

morris.o: morris.cpp morris.hpp

morris_plus.o: morris_plus.cpp morris_plus.hpp

clean:
	-rm *.o run_morris_plus_simulation_01 run_morris_plus_simulation_02