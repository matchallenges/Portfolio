#include <cstdio>
#include <iostream>

enum class Operation{
    Add,
    Subtract,
    Multiply,
    Divide
};

struct Calculator{
    
    
    Calculator(Operation calc_input){
        if (calc_input == Operation::Add) flag = 0;
        if (calc_input == Operation::Subtract) flag = 1;
        if (calc_input == Operation::Multiply) flag = 2;
        if (calc_input == Operation::Divide) flag = 3;
    }

    int calculate(int a, int b){
        if(flag == 0) return a + b;
        if(flag == 1) return a - b;
        if(flag == 2) return a * b;
        if(flag == 3) return a / b;
        return 0;
    }
    private:
        int flag{};
};

using namespace std;

int main(){
    Calculator calc{ Operation::Subtract };
    cout << calc.calculate(7, 9);
}