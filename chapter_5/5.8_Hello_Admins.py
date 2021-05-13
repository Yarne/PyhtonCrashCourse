names1 = ['jaden', 'dirk', 'admin', 'user', 'blaat']
names = []

if names:
    for name in names:
        if name == 'admin':
            print('Hello Admin, would you like a status report?')
        else:
            print(f'Hello {name.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')
