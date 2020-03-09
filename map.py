
users = {1: 'jack', 2: 'rose', 3: 'jack', 4: 2}

for index, user in users.items():
    print(index, user)
print(list(users.keys()))
print(list(users.values()))
print(set(users.values()))
