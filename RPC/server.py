import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def	suma_remota(a, b):
	return a+b

server = SimpleXMLRPCServer(("localhost", 8080))
server.register_function(suma_remota, "suma")
print ("soy el servidor y estoy corriendo por el pueto 8080")
server.serve_forever()


