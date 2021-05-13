places = ['rome', 'dublin', 'praag', 'shanghai', 'madrid']
print(f'{places}\n')

print(sorted(places))
print(places)

print(f'\n{sorted(places, reverse=True)}')
print(places)

places.reverse()
print(f'\n{places}')

places.reverse()
print(places)

places.sort()
print(f'\n{places}')

places.sort(reverse=True)
print(places)
