#include <stdio.h>

/*  */

/* print the Frenheit-Celsius conversion table
    for fahr = 0, 20, ..., 300 */ 

int main()
{
    /* code goes here */

    int fahr, celsius; /* initialize the temperature integers */
    int lower, upper, step; /* initialize the flow control integers */

    lower = 0; /* lower limit of temperature size */
    upper = 300; /* upper limit */
    step = 20; /* step size (intervals) */

    fahr = lower; /* assign fahr to the integer lower */
    while (fahr <= upper) { /* while fahr is less than or equal to upper */
        celsius = 5 * (fahr-32) / 9; /* each loop celsius will be converted from the fahr variable */
        printf("%d\t%d\n", fahr, celsius); /* print formatting where %d specifies an integer argument, with the arguments proceeding */ 
        fahr = fahr + step; /* increments fahr by the step */ 
   } 

}