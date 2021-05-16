dream_vacations = {}

while True:
    username = input("What's your name?: ")
    dream_vacation = input("What's your dream vacation?: ")

    if (username or dream_vacation) == "quit":
        break

    dream_vacations[username] = dream_vacation

    user_continue = input("Does anyone else want to share their dream vacation? (yes/no): ")
    if user_continue == "yes":
        continue

    for user, destination in dream_vacations.items():
        print(f"{user.title()} want's to go to {destination.title()}.")
    break
