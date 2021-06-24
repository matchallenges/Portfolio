/* if (boolean-expression) -> statement

if (boolean-expression-1) statement-1
else if (boolean-expression-2) statement-2
else statement-3

return -> evaluted variable

*/

#include <cstdio>

int main(){
    int x = 0;
    if (x > 0) printf ("Positive.");
    else if (x < 0) printf ("Negative.");
    else printf("Zero.");
}