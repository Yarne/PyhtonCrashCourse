current_users = ['jaden', 'Dirk', 'admin', 'user', 'blaat']
new_users = ['jos', 'alex', 'dirk', 'eva', 'User']

current_users_lower_case = [current_user.lower() for current_user in current_users]

for user in new_users:
    if user.lower() in current_users_lower_case:
        print(f"'{user}' is not available!")
    else:
        print(f"'{user}' is available.")
