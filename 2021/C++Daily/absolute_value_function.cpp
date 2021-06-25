#include <cstdio>
#include <iostream>

//function
int absolute_value_function(int x){
    int ret = 0;
    if (x >= 0) ret = 0;
    else ret = x * -1;
    return ret;
}

//driver code

using namespace std;

int main(){
    cout << absolute_value_function(-56);
}