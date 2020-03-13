with open("./class.py") as f:
    content = f.read()
    print(content)

with open("./class.py") as f:
    for item in f:
        print(content)

with open("./class.py") as f:
    lines = f.readlines()

print(lines)

with open("./class.py") as reader:
    with open("./write.py", "w") as writer:
        content = reader.read()
        writer.write(content)
