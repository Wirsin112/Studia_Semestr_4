from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 8888))
answer = "3;Janhaslo"
s.send(str(["LOG","ROCH", "Pawlak"]).encode())
data = s.recv(1024)
print(data.decode())
s.close()
