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

    data = client.recv(1024)
    if eval(data.decode())[0] is "LOG":
        db = TinyDB('Login.json')
        User = Query()
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
        client.send("OK".encode())
        client.close()
    if eval(data.decode())[0] is "CON":
        kubs.append(client)
    if eval(data.decode())[0] is "GCL":
        from tinydb import TinyDB, Query
        nazwy = TinyDB('ListaChatow.json')
        User = Query()
        a = nazwy.search(User.name != "")
        b = []
        for i in a:
            b.append(i["name"])
        print(b)
        client.send(str(b).encode())
        client.close()
    if eval(data.decode())[0] is "CHECKCON":
        i = 0
        while i < len(kubs):
            try:
                kubs[i].send(eval(data.decode())[1].encode())
                i += 1
            except ConnectionResetError:
                del kubs[i]
                print(kubs)


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)
while True:
    client,addr = s.accept()
    print("Witamy w koloni", addr)
    start_new_thread(clientThread, (client,))
s.close()