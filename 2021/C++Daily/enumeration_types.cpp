#include <cstdio>
#include <iostream>

enum class Employees {
    Mathieu,
    Marc,
    Connor,
    Sam,
};

int count_employees(){
    unsigned int c = 0;
    for(int i; i < sizeof(Employees); i++){
        c = i;
    }
    return c + 1;
}

int main(){
    std::cout << count_employees();
}


