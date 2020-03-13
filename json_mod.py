import json


def load_file():
    with open('./user.json') as f:
        val = json.load(f)
        print(val)


if __name__ == '__main__':
    load_file()


def dump_file():
    with open('./new_user.json', 'w') as f:
        user = {'name': 'jack', 'age': 11}
        json.dump(user, f)


if __name__ == '__main__':
    dump_file()


if __name__ == '__main__':
    users = {"name": "jack", "age": 11}
    val = json.dumps(users)
    print(val)
    user = json.loads(val)
    print(user)
