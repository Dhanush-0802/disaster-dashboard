with open("notes.txt", "w") as f:
    f.write("hello, this is my first python file.\n")

with open("notes.txt", "r") as f:
    content = f.read()

print("file content:\n", content)