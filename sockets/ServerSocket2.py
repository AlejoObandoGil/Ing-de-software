import socket  
  
s = socket.socket()   
s.bind(("localhost", 8001))  
s.listen(1)  
print ("Hola, soy el SERVIDOR")  
sc, addr = s.accept()  

while True:  
      recibido = sc.recv(1024)  
      if recibido == "Salir":  
         break        
      print ("Recibido:", recibido)  
        
print ("Pasalo bien, te extraNaremos")  
  
sc.close()  
s.close()  