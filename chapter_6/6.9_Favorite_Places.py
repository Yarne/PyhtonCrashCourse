favorite_places = {
    'elon': ['paris', 'berlin'],
    'vladimir': ['china'],
    'trump': ['murica', 'china', 'russia']
    }

for person, places in favorite_places.items():
    if len(places) <= 1:
        print(f'\nThe favorite place of {person} is {places[0].title()}.')
    else:
        print(f'\nThe favorite place of {person} are:')
        for place in places:
            print(place.title())
