from socket import *
from datetime import datetime
from _thread import *
import threading
from tinydb import TinyDB, Query
from tinydb import TinyDB, Query
kubs = []

def Get_Server_Time():
    return datetime.now().strftime("%H:%M:%S")

threading_lock = threading.Lock()



def clientThread(client):
    global kubs
    db = TinyDB('Login.json')

    User = Query()
    data = client.recv(1024)
    if eval(data.decode())[0] is "LOG":
        a = db.search(User.name == eval(data.decode())[1] and User.password == eval(data.decode())[2])
        if len(a) == 1:
            client.send("OK".encode())
        else:
            client.send("ERR".encode())

    if eval(data.decode())[0] is "REG":
        db.insert({"login": eval(data.decode())[1], "password": eval(data.decode())[2]})
        client.send("OK".encode())
        client.close()
    if eval(data.decode())[0] is "EXI":
        client.close()
    if eval(data.decode())[0] is "SND":
        i = 0
        time = Get_Server_Time()
        a = ["MES",eval(data.decode())[1],eval(data.decode())[2],time,eval(data.decode())[3]]
        them = db.table(eval(data.decode())[3])
        them.insert({"user": eval(data.decode())[1], "message": eval(data.decode())[2], "time": time})
        print("2")
        while i < len(kubs):
            try:
                kubs[i].send(str(a).encode())
                i += 1

            except ConnectionResetError:
                del kubs[i]

        client.close()
    if eval(data.decode())[0] is "CON":
        kubs.append(client)
        print("in")
    if eval(data.decode())[0] is "GCL":
        chats = db.table("Them")
        a = chats.search(User.name != "")
        b = []
        for i in a:
            b.append(i["name"])
        print(b)
        client.send(str(b).encode())
        client.close()
    if eval(data.decode())[0] is "GMP":
        chats = db.table(eval(data.decode())[1])
        a = chats.all()
        print(a)
        client.send(str(a).encode())
        client.close()

    if eval(data.decode())[0] is "NTA":
        chats = db.table("Them")
        i = 0
        a = ["CAT"]
        a.append(eval(data.decode())[1])
        while i < len(kubs):
            try:
                kubs[i].send(str(a).encode())
                i += 1
            except ConnectionResetError:
                del kubs[i]
        chats.insert({"name":eval(data.decode())[1]})
        client.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)
while True:
    client,addr = s.accept()
    print("Witamy w koloni", addr)
    start_new_thread(clientThread, (client,))
s.close()