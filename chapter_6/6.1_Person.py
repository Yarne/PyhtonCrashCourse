user_information = {
    'first_name': 'yarne',
    'last_name': 'snyers',
    'age': 22,
    'city': 'beringen',
    }

for information in user_information.values():
    if isinstance(information, str):
        print(information.title())
    elif isinstance(information, int):
        print(information)
