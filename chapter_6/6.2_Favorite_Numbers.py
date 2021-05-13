favorite_numbers = {
    'jan': [2, 5],
    'jos': [9, 34],
    'robert': [42],
    'henk': [22, 76],
    'karel': [84]
    }

for name, favorite_number in favorite_numbers.items():
    if len(favorite_number) == 1:
        print(f"{name.title()}'s favorite number is {favorite_number[0]}.")
    else:
        print(f"{name.title()}'s favorite number are:")
        for number in favorite_number:
            print('\t', number)
