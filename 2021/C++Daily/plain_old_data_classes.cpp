#include <cstdio>
#include <iostream>

struct Rocket{
    char name[64];
    int size;
    int weight;
    int capacity;
    bool ready_for_take_off;
};

int main(){
    Rocket DeepSamOrbit;
    DeepSamOrbit.size = 2;
    DeepSamOrbit.weight = 3000;
    DeepSamOrbit.capacity = 6;
    DeepSamOrbit.ready_for_take_off = true;
    std::cout << DeepSamOrbit.ready_for_take_off;
}