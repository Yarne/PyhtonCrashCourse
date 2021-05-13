favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

voters = ['jen', 'sarah', 'jos', 'edward', 'eric', 'timmy', 'phil']

for voter in voters:
    if voter in favorite_languages.keys():
        print(f'Thank you {voter.title()} for voting.')
    else:
        print(voter.title(), 'you should vote!')
