import threading

class MyThread(threading.Thread):
    def __init__(self,x,ini,final):
        super(MyThread, self).__init__()
        self.base = x
        self.limiteinf = ini
        self.limitesup = final
        
	
    def potencia(self, base, exp):
        if exp==0:
            return 1
        else:
            return self.potencia(base, exp-1)*base
    
    def suma_potencia(self, inicio, fin):
        suma=0
        for i in range(inicio, fin+1):
            suma=suma+self.potencia(self.base,i)
    
    def run(self):
        return self.suma(self.limiteinf, self.limitesup)
        
        
 






 
