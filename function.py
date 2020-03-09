
def say_hello(aaa, *args, **kwargs):
    print(aaa)
    print(args)
    print(kwargs)


def multi_args(name, age):
    print("name", name)
    print("age", age)


if __name__ == '__main__':
    multi_args("hello", 11)
    multi_args(age=11, name="jack")


def default_arg(name, animal_type="dog"):
    print("name", name)
    print("animal_type", animal_type)


if __name__ == '__main__':
    default_arg("jack")


users = ['jack', 'rose', 'mini']


def list_arg(users_arg):
    users_arg.append("rookie")


if __name__ == '__main__':
    list_arg(users[:])
    print(users)


