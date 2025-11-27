def check_minutes(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    time = (f'{minutes} minutes is {seconds} seconds {hours} hours')
    return time

print(check_minutes(30))
    
def check_length(word):
    count = 0
    for letter in word:
        count += 1
    return count

print(check_length('Topseen'))

def get_vowel(word):
    for letter in range(1, 27):
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1            
            return letter

print(get_vowel('apple'))
