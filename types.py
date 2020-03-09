import typing


def add(x: int, y: int) -> int:
    return x + y


add(1, 2)


def append(own_list: typing.List[int], val):
    own_list.append(val)


users: typing.List[float] = [1.1, 2, 3]
append(users, 4)
print(users)


