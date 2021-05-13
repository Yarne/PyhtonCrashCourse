glossary = {
    'append(x)': 'Add an item to the end of the list.',
    'insert(i, x)': 'Insert an item at a given position.',
    'remove(x)': 'Remove the fist item form the list whose value is equal to x.',
    'pop[i]': 'Remove the item at the given position in the list.',
    'clear()': 'Remove all items from the list.'
    }

for word, meaning in glossary.items():
    print(word, ': ', meaning, sep='')
