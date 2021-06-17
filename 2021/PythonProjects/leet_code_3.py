def reverse(x: int ) -> int:
    ret = 0

    print([int(y) for y in str(-x)])


    if x < 0: # if x is less than 0
        for i in range(len([int(y) for y in str(-x)])): # for loop runs for the length of the list and typecasts the elements of the list to integers and typecasts the integer to a string to iterate over it   
            ret += [int(n) for n in str(-x)][i]*10**(i) # increment ret by the ith element times 10 exponent element number 
        ret = ret*(-1) # take the reciprocal of the integer
        print(ret)

reverse(-91)