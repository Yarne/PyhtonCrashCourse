user0 = {
    'first_name': 'yarne',
    'last_name': 'snyers',
    'age': 22,
    'city': 'beringen',
    }

user1 = {
    'first_name': 'jos',
    'last_name': 'mertens',
    'age': 46,
    'city': 'hasselt',
    }

user2 = {
    'first_name': 'elon',
    'last_name': 'musk',
    'age': 50,
    'city': 'murica',
    }

users = [user0, user1, user2]

for user in users:
    print()
    for user_information in user.values():
        if isinstance(user_information, str):
            print(user_information.title())
        else:
            print(user_information)
