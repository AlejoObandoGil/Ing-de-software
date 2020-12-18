import socket                                                           
import threading
import sys
import pickle

class Servidor():

    def __init__(self, host="localhost", port=3000):                    #recibe los parametros direccion de host y puerto

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #familia de socket y tipo de socket
        self.sock.bind((str(host), int(port)))                          #conectamos con el cliente
        self.sock.listen(10)                                            #numero de clientes o conexiones
        self.sock.setblocking(False)

        self.clientes = []

        aceptar = threading.Thread(target=self.aceptarCon)              #hilo que acepta conexiones
        procesar = threading.Thread(target=self.procesarCon)            #hilo que procesa conexiones

        aceptar.daemon = True                                           #ligado al hilo principal
        aceptar.start()
        procesar.daemon = True                                          #ligado al hilo principal
        procesar.start()

        while True:                                                     #ciclo del hilo principal
            msg = input('->')                                           
            if msg == 'salir':                                          #Si el mensaje es igual a salir, cerramos conexion del socket
                self.sock.close()                                           
                sys.exit()
            else:
                pass

    #------Metodo que envia mensaje a todos los clientes-----
    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:                                        #el cliente que recibe debe ser diferente al que envia
                    c.send(msg)                                         #si es asi se envia el mensaje. No es necesario serializar
            except:
                self.clientes.remove(c)                                 #si ocurre un error de conexion eliminamos el cliente

    #------Metodo que acepta las conexiones-----
    def aceptarCon(self):
        print("Conexion habilitada...")
        while True:
            try:
                conn, addr = self.sock.accept()                         #conexiones y direccion de clientes
                conn.setblocking(False)
                self.clientes.append(conn)                              #agregamos conexion de cliente a la lista
            except:
                pass

    #-----Metodo que procesa las conexiones-----
    def procesarCon(self):
        print("Conexion con el Servidor incializada...")
        while True:
            if len(self.clientes) > 0:                                  #pregunta si hay clientes
                for c in self.clientes:                                         
                    try:
                        data = c.recv(1024)                             #mensaje recibido
                        if data:                                        #si el cliente recibe un mensaje    
                            self.msg_to_all(data,c)                     #llamamos un metodo que envia el mensaje a los demas clientes
                    except:
                        pass

s = Servidor()
