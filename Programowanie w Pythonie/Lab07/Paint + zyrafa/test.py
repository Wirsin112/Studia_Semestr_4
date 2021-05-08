from tinydb import TinyDB, Query
nazwy = TinyDB('db.json')
User = Query()
a = nazwy.search(User.name != "")
print(a)
b = []
for i in a:
    b.append(i["name"])
print(b)