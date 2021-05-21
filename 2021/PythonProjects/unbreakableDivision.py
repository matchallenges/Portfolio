# input an integer input for numerator
try:
    a = float(input("type a number: "))
except NameError:
    print("Error Message: type an integer please!")
    exit()
except SyntaxError:
    print("Error Message: type an integer please!")
    exit()
except TypeError:
    print("Error Message: type an integer please!")
    exit()

# input an integer input for denominator
try:
    b = float(input("type another number: "))
except NameError:
    print("Error Message: type an integer please!")
    exit()
except SyntaxError:
    print("Error Message: type an integer please!")
    exit()
except TypeError:
    print("Error Message: type an integer please!")
    exit()

try:
    print(float(a/b))
except ZeroDivisionError:
    print("Error Message: the integers cannot be divided by zero. Try again")
    exit()
except NameError:
    print("Error Message: cannot divide")
    exit()
except SyntaxError:
    print("Error Message: type an integer please!")
    exit()
except TypeError:
    print("Error Message: type an integer please!")
    exit()

