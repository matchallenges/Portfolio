#include <cstdio>

int sum_unsigned_nums(unsigned int x, unsigned int y){
    unsigned int z = x + y; 
    return z;
}


int main(){
    printf("%x", sum_unsigned_nums(1, 1));
}