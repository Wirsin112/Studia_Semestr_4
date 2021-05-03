import os
def generator(n,rozszerzenie):
    for i in os.listdir(f"{n}"):
        if i.endswith(rozszerzenie):
            yield i

path = "."
for i in generator(path,'.py'):
    print(i)