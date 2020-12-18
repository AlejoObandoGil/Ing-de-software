import socket  
  
s = socket.socket()   
s.connect(("localhost", 8001))  
print ("Amigo, ingresa un mensaje para el servidor: ") 
while True:  
      mensaje = input("mensaje: ")  
      mensaje = str(mensaje)
      s.send(mensaje)  
      if mensaje == "Salir":  
         break  
  
print ("que tengas una linda tarde")  
  
s.close()  