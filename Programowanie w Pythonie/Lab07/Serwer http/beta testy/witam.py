from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 8888))
s.send(str(["CHECKCON","ROCH", "Pawlak"]).encode())
s.close()
