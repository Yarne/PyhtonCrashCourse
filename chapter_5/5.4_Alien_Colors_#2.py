def alien_points(color):
    points = int

    if color == 'green':
        points = 5
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 15

    print(f'You earned {points} points.')


alien_colors = ['green', 'yellow', 'red', 'blue']

for alien_color in alien_colors:
    alien_points(alien_color)
