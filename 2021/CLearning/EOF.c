 #include <stdio.h> 

  /* prints EOF */

  int main(){

    int c;

    while ((c = getchar()) != EOF)
        printf("%d", EOF); 
 }