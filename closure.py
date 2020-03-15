def outer():
    count = 0

    def inner_fn():
        nonlocal count
        count += 1
        return count

    return inner_fn


inner = outer()
print(inner())
print(inner())
print(inner())
print(inner())
print(inner())
