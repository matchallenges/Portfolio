 #include <stdio.h> 

/* copy input to output; 1st version  */ 

int main(){

    int c; /* needed to hold the characters and EOF  */ 

    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}

/* research both functions */