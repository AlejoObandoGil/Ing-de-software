import socket  
 
s = socket.socket()   
s.connect(("localhost", 8001))  
mensaje=input('ingrese el mensaje: ')
s.send(mensaje) 
s.close()  