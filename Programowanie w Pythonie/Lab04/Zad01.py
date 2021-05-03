def make_dict(string):
    dict = {}
    tab = string.strip().split("\n")
    for x in tab:
        dict[x.split(":")[0]] = x.split(":")[1].strip()
    return dict
str = """
a:1
c:1
"""
print(make_dict(str))