import threading
import time

class MyThread(threading.Thread):
	def __init__(self,x,y,op):
		super(MyThread, self).__init__()
		self.num1=x
		self.num2=y
		self.op=op

	def suma(self):
		return self.num1+self.num2
	def resta(self):
		return self.num1-self.num2
	def mult(self):
		return self.num1*self.num2
	def divi(self):
		return self.num1/self.num2

	def run(self):
		if self.op==1:
			print ("la suma es:"+str(self.suma()))
		if self.op==2:
			print ("la resta es: "+str(self.resta()))
		if self.op==3:
			print ("la multiplicacion es: "+str(self.mult()))
		if self.op==4:
			print ("la division es:"+str(self.divi()))



