prompt = "Which pizza topping do you want?"

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"I'll add {topping} to the pizza.\n")
