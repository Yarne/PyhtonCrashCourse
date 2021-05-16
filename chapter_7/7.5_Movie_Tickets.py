prompt_age = "What's your age?"

while True:
    user_input = input(prompt_age)
    if user_input == "quit":
        break
    else:
        age = int(user_input)

    if age < 3:
        print("You can go for free!\n")
    elif age <= 12:
        ticket_price = 10
        print(f"That'll be {ticket_price} dollars.\n")
    else:
        ticket_price = 15
        print(f"That'll be {ticket_price} dollars.\n")
