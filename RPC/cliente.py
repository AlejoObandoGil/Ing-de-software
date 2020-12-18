import xmlrpclib  
a =input(str('Ingrese el primer numero: '))
b=input(str('Ingrese el segundo numero: '))
proxy = xmlrpclib.ServerProxy("http://localhost:8080/")
print ("La suma es: " +str(proxy.suma(a,b)))



