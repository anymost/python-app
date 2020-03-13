try:
    a = 1/0
except ZeroDivisionError:
    print("zero division")
else:
    print("ok")
finally:
    print("good")

