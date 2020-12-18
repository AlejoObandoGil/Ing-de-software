# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:27:26 2020
clase sistemas distribuidos

@author: Usuario UTP
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
#from xmlrpc.server import SimpleXMLRPCServer

class funciones_rpc:
    def suma(self, p, q):
        return p+q
    def resta(self, p, q):
        return p-q

    def multi(self, p, q):
        return p*q
    
    def divi(self, p, q):
        return p/q
server = SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(funciones_rpc())
print("soy un servidor implementado con clases")
server.serve_forever()

