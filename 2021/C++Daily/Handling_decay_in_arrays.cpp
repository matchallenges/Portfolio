#include <cstdio>
#include <iostream>

struct College{
    char name[256];
};

void print_names(College* colleges, size_t n_colleges){
    for (size_t i = 0; i < n_colleges; i++){
        printf("%s College\n", colleges[i]);
    }
}

int main(){
    College oxford[] = {"Magdalen", "Nuffield", "Kellog"};
    print_names(oxford, sizeof(oxford) / sizeof(College));
}