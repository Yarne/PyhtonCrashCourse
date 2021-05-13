my_pizzas = ['margarita', 'salami', 'hesp']
friends_pizzas = my_pizzas[:]

my_pizzas.append('kebab')
friends_pizzas.append('kaas')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza.title())
