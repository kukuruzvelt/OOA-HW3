from random import randint
import os
import timeit


def generateFile(filename):
    with open(filename, "w") as f:
        while os.stat(filename).st_size < 50 * 1024 * 1024:
            print(randint(0, 100), file=f)



# generateFile(FILE_NAME)

a = """
with open("docs/text.txt") as f:
    s = 0
    lines = f.readlines()
    for line in lines:
        if line.strip().isdigit():
            s += int(line.strip())
"""
print(timeit.timeit(a, number=10))

b = """
with open("docs/text.txt") as f:
    s = 0
    for line in f:
        if line.strip().isdigit():
            s += int(line.strip())
"""
print(timeit.timeit(b, number=10))

c = """
with open("docs/text.txt") as f:
    s = (int(line.strip()) for line in f if line.strip().isdigit())
"""

print(timeit.timeit(c, number=10))
