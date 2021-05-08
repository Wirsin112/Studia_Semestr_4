from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 8888))
answer = "y"
while answer is "y":
    s.send(answer.encode())
    data = s.recv(1024)
    print("godzina dolaczenia", data.decode())
    answer = input("Powtorzyc?\n")
s.close()
