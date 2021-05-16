sandwich_orders = ["smos", "pastrami", "salami", "kaas", "pastrami", "tonijn", "pastrami"]
finished_sandwiches = []

if "pastrami" in sandwich_orders:
    print("We've run out of pastrami.\n")
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThese sandwiches are finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())