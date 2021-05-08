from socket import *
def Listen_Server():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 8888))
    answer = str(["CON"])
    s.send(answer.encode())
    while 1:
        try:
            data = s.recv(1024)
            if data:
                print(data.decode())
        except(error):
            pass
    s.close()
