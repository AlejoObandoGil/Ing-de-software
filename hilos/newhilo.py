import threading
import time

class MyThread(threading.Thread):
    def __init__(self,x,y):
        super(MyThread, self).__init__()
        self.num1 = x
        self.num2 = y
	
    def suma(self, a, b):
        return a+b

    def run(self):
        print (str(self.suma(self.num1, self.num2)))

n=int(input('amiguito ingresa el primer numero: '))
m=int(input('amiguito ingresa el segundo numero: '))
t = MyThread(n,m)
t.start()
