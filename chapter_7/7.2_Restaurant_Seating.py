prompt = "How many people are in the dining group?"
dining_group_size = int(input(prompt))
if dining_group_size > 8:
    print("You'll have to wait for a table.")
else:
    print("We have a table ready.")
