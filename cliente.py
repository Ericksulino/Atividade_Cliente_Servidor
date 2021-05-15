import socket
ip = 'localhoust'
port = 8000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(addr)
while(True):
    mensagem = input('digite uma mensagem para enviar ao servidor: ')
    client_socket.send(mensagem.encode())
    print('mensagem enviada')
    print(client_socket.recv(1024).decode())
client_socket.close()