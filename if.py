
a = '1'
b = '2'
if a == '1':
    print("a == 1")

if a == '1' and b == '2':
    print('double true')

num_list = [1, 2, 3, 4]

if 1 in num_list:
    print('1 in num_list')

if 5 not in num_list:
    print("5 no in num_list")


val = a == '2'
if not val:
    print("hello")

conditional_list = [x for x in range(10) if x > 0]
print(conditional_list)

for index, item in enumerate(conditional_list):
    print(index, item)

