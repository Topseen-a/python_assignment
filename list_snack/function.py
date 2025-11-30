def check_list():
    return list(range(1, 16))

def add_third_element(number):
    total = 0
    for count in range(2, len(number), 3):
        total += number[count]
    return total


