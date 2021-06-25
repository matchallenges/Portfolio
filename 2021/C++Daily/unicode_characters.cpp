#include <cstdio>
#include <iostream>

using namespace std;

int main(){
    
    cout<<"₿";
    wchar_t y = L'\u0020';
    wchar_t z = L'\u0025';

    printf("%lc %lc", y, z);
}