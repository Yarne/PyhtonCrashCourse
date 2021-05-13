major_rivers = {
    'volga': 'russia',
    'thanlyin': 'china',
    'niger': 'guinea'
    }

for river, country in major_rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print()

for river in major_rivers.keys():
    print(river.title())

print()

for country in major_rivers.values():
    print(country.title())
