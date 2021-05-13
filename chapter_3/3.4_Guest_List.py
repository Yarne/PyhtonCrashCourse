guests = ['dirk', 'jan', 'alex']
print(guests)


def invitations(invitees):
    for invitee in invitees:
        print(f'\nDear {invitee.title()}\nYou are invited to come to dinner next saturday. \nKind regards')
    print('\n')


invitations(guests)

cancel = 'jan'
print(cancel)

guests.remove(cancel)
print(guests)

guests.append('jos')
print(guests)

invitations(guests)


print('We found a bigger table and are inviting more guests.')

print(guests)

guests.insert(0, 'eric')
print(guests)

guests.insert(round(len(guests)/2), 'jaap')
print(guests)

guests.append('joost')
print(guests)

invitations(guests)


print("The table won't arrive in time. Only two guests can come")

for remove in range(0, 4):
    removed = guests.pop()
    print(f"\nDear {removed.title()}\nYou can't come.")

print(guests)

for invited in guests:
    print(f'\nDear {invited.title()}\nYou can still come.')

print(guests)
del(guests[:len(guests)])
print(guests)

print(len(guests))
