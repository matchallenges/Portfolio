//variable adresses

#include <cstdio>

using namespace std;

int main(){
    int amount_of_apples{};
    int* amount_of_apples_adress = &amount_of_apples;
    printf("Value using derefrencing: %d\n", *amount_of_apples_adress);
    printf("Variable adress: %p\n", amount_of_apples_adress);
    *amount_of_apples_adress = 17325;
    printf("Value using derefrencing: %d\n", *amount_of_apples_adress);
    printf("Variable adress: %p\n", amount_of_apples_adress);
    
}