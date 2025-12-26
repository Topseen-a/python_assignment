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


