from socket import *
from datetime import datetime
from _thread import *
import threading
from tinydb import TinyDB, Query
Kubs= []
import time

def Get_Server_Time():
    return datetime.now().strftime("%H:%M:%S")


threading_lock = threading.Lock()
def clientThread(client):
    global Kubs
    db = TinyDB('Login.json')
    User = Query()
    data = client.recv(1024)
    if eval(data.decode())[0] is "LOG":
        a = db.search(User.name == eval(data.decode())[1] and User.password == eval(data.decode())[2])
        if len(a) == 1:
            client.send("OK".encode())
        else:
            client.send("ERR".encode())
        print("Start")

    if eval(data.decode())[0] is "REG":
        db.insert({"login": eval(data.decode())[1], "password": eval(data.decode())[2]})
        client.close()
    if eval(data.decode())[0] is "EXI":
        print("Koniec")
        client.close()
    if eval(data.decode())[0] is "SND":
        client.raddr = ('127.0.0.1', 666)
        client.send("ok".encode())
        client.close()
    if eval(data.decode())[0] is "CON":
        Kubs.append(client)
    if eval(data.decode())[0] is "CHECKCON":
        print(type(Kubs[0]))
        Kubs[0].send("ok".encode())



s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)
while True:
    client,addr = s.accept()
    print(type(client))
    print("Witamy w koloni", addr)
    start_new_thread(clientThread, (client,))
s.close()