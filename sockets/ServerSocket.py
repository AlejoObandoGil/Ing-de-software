import socket

Mi_socket=socket.socket()
Mi_socket.bind(("localhost", 8001))
Mi_socket.listen(1)  
print ("Servidor arriba, pero triste porque no tengo conexiones. pero sigo escuchando!!!!!")
cli, addr=Mi_socket.accept()
recibido = cli.recv(1024)  
print ("mensaje recibido: ", recibido)
print("cliente, te tenenos detectado!!!!:")
print("tu direccion ip es: ", addr[0])
print("tu puerto de conexion es: ", addr[1])

cli.close()
Mi_socket.close()  
