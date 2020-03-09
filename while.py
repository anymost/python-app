while True:
    value = input('please input:\n')
    try:
        print(float(value))
    except ValueError:
        print(ValueError)
    if value == 'ok':
        break
