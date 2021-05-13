numbers = range(1, 10)

for number in numbers:
    if number > 3:
        ordinal = 'th'
    elif number > 2:
        ordinal = 'rd'
    elif number > 1:
        ordinal = 'nd'
    else:
        ordinal = 'st'

    print(number, ordinal, sep='')
