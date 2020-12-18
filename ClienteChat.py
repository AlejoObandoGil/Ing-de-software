import socket                                                           
import threading
import sys
import pickle

class Cliente():

    def __init__(self, host="localhost", port=3000):                    #recibe los parametros direccion de host y puerto

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #familia de socket y tipo de socket
        self.sock.connect((str(host), int(port)))                       #coneccion al servidor

        msg_recv = threading.Thread(target=self.msg_recv)               #hilo que recibe los mensajes

        msg_recv.daemon = True                                          #ligado al hilo principal
        msg_recv.start()

        while True:                                                     #ciclo del hilo principal
            msg = input('->')                                           
            if msg != 'salir':                                          #Si el emsanje es diferente a salir llamamos el metodo enviar
                self.send_msg(msg)
            else:
                self.sock.close()                                       #si no cerramos conexion del socket
                sys.exit()

    #Metodo que recibe mensajes
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)                             #Mensaje que llega del socket max 1024 caracteres
                if data:
                    print(pickle.loads(data))                           #mensaje des-serializado 
            except:
                pass

    #Metodo que envia mensajes
    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))                               #mensaje serializado


c = Cliente()