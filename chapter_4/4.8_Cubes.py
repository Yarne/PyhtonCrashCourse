cubes = [number**3 for number in range(1, 10)]

for cube in cubes:
    print(cube)

print('\nThe first three items in the list are:')
print(cubes[:3])

print('\nThree items from the middle of the list are:')
print(cubes[round(len(cubes)/2)-1:round(len(cubes)/2)+2])

print('\nThe last three items in the list are:')
print(cubes[-3:])
