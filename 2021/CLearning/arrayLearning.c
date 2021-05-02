#include <stdio.h>

int main() {

    int c, i;
    int ndigits[10];

    for (i = 0; i < 10; ++i)
        ndigits[i] = 0;
    
    while ((c = getchar()) != EOF)
       if (c >= '0' && c <= '9')
            ++ndigits[c];
    
    printf("digits ="); 
    for (i = 0; i < 10; ++i)
        printf(" %d", ndigits[i]);
    
}

/* work on array knowledge and figure this program out bro! */ 