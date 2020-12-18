import threading

class MyThread(threading.Thread):
    def __init__(self,ini,final):
        super(MyThread, self).__init__()
        self.inicio = ini
        self.factoN = final
    def factorial(self,n):
        if n==0:
            return 1
        else:
            return self.factorial(n-1)*n
    def suma_factoriales(self,inicia,tope):
        suma_f=0
        for i in range (inicia,tope):
            suma_f=suma_f+self.factorial(i)
        return suma_f
    
    def run(self):
        return self.suma_factoriales(self.inicio, self.factoN)
        