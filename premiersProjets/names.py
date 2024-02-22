
names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())
"""
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""
for name in sorted(names):
    print(f"hello, {name}")