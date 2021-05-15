import socket
host = 'localhost'
port = 8000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)
print("aguardando conexão...")
con, cliente = serv_socket.accept()
print("conectado")
print("aguardando mensagem...")

while(True):
    recebe = con.recv(1024)
    con.send('teste'.encode())
    print('mensagemrecebida: '+ recebe.decode())
serv_socket.close()