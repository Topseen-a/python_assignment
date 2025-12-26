import math

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def get_positive_difference(first_number,second_number):
    if first_number > second_number:
        return first_number - second_number
    else:
        return second_number - first_number

def get_division(first_number,second_number):
    if second_number == 0:
        return 0
    else:
        return first_number / second_number

def factor_of(number):
    factor = 0
    for count in range(1, number +1):
        if number % count == 0:        
            factor += 1
    return factor

def is_square(number):
    result = math.sqrt(number)
    if (result * result == number):
        return True
    else:
        return False

print(is_square(5))
