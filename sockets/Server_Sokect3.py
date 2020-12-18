import socket
import time

Mi_socket=socket.socket()
Mi_socket.bind(("localhost", 8001))
Mi_socket.listen(1)  
print ("Soy el servido, vamos a intercambiar mensajes!!!!!")
cli, addr=Mi_socket.accept()
recibido = cli.recv(1024)
print("conectado: "+recibido)  
'''
nombre=recibido
ip= addr[0]
puerto= [1]
fecha= time.strftime("%x")
hora =  time.strftime("%X")
datos=[nombre, ip, puerto, fecha, hora]
cli.send(datos)
'''
cli.send("BIENVENIDO: "+recibido)
cli.close()
Mi_socket.close()  