cities = {
    'tokyo': {'country': 'japan', 'population': 13_929_280, 'fact': 'Tokyo is the largest metropolitan area.'},
    'berlin': {'country': 'germany', 'population': 3_645_000, 'fact': "Berlin is Germany's capital."},
    'hasselt': {'country': 'belgium', 'population': 70_000, 'fact': "It's cool."}
}

for city, information in cities.items():
    print(city.title(), information['country'].title(), f"{information['population']: ,}", information['fact'],
          sep=', ')
