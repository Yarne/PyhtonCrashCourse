pet0 = {'animal': 'dog', 'owner': 'vladimir'}
pet1 = {'animal': 'parrot', 'owner': 'trump'}
pet2 = {'animal': 'bunny', 'owner': 'pol'}

pets = [pet0, pet1, pet2]

for pet in pets:
    print()
    for key, value in pet.items():
        print(f'{key.title()}: {value.title()}')

print()

for pet in pets:
    print(pet['owner'].title(), 'has a', pet['animal'].title(), end='.\n')
