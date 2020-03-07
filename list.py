
num_list = [1, 2, 3, 4, 5]

print(num_list)

num_list.insert(0, 0)

print(num_list)

del num_list[0]

print(num_list)

num_list.sort(reverse=True)

print(num_list)

print(len(num_list))

print(num_list[-1])

for item in reversed(num_list):
    print(item)

for item in range(1, 5):
    print(item)

print(list(range(10)))
print([x ** 2 for x in range(10)])

new_list = list(range(1, 10))

print(new_list[:])
print(new_list[0: -1])

new_tuple = (1, 2)
print(new_tuple)

