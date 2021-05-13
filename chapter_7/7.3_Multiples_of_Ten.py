prompt = "Give a number: "
given_number = int(input(prompt))
if given_number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number isn't a multiple of 10.")
