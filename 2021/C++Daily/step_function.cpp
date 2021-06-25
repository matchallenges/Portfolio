#include <cstdio>

int step_function(int x){
    int result = 0;
    if (x < 0) result = -1;
    else if (x > 0) result = 1;
    else result = 0;
    return result;
}

int main(){
    int num1 = 42;
    int num2 = -5;
    int num3 = 0;
    printf("%d %d %d", step_function(num1), step_function(num2), step_function(num3));
}

//Three uses of the step_function