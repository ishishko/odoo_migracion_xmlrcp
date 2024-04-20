#!/usr/bin/python3
import sys
from xmlrpc import client


# --- Para importar contactos ---
class CreateXMLRCP:

    def __init__(self, url, dbname, user, pwd, model) :
        self.url = url
        self.dbname = dbname
        self.user = user
        self.pwd = pwd
        self.model = model
        self.common = ""
        self.userID = ""
        self.models = ""
        self.start = self.__start()

    # --Test conexion y UserID--
    def __start(self):
        self.common = client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        print('--------------------------------------------------------------')
        print ('Test: Conexion OK. Server:', self.common)
        self.userID = self.common.authenticate(self.dbname,self.user,self.pwd,{})
        print ("COMMON OK. Usuario Autenticado. User ID:", self.userID)
        self.models = models = client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        print ('MODELS OK. Models:', self.models)
        print('--------------------------------------------------------------')
    
    # --Obtener IDs--
    def search_ids(self, conditions=[['name', '!=', '']]):
        data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, 'search', 
        [conditions])
        print("Obtener registros OK. Registros obtenidos:", len(data))
        return data
    
    # ---Leer Campos de lista de IDs---
    def read_data(self, ids_list, field_list = ['name','street'] ):
        print('--------------------------------------------------------------')
        print("----- Obteniedo datos de lista -----")
        data = []
        n = 0
        for id in ids_list:
            item = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
                   'read', [[id], field_list ])
            data.append(item)
            n = n + 1
            if n % 100 == 0: print('>>>>> Obtenidos',n, 'de', len(ids_list))
            if n == 1: break
        print('----- Obtener Finalizado -----')
        print('----- Se han obtenido', n , 'de' , len(ids_list),'Registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', data[n-1], '<<<<<')
        print('--------------------------------------------------------------')
        return data
    
    # ---Leer Campos de lista de IDs---
    def create_reg(self, data):
        print('--------------------------------------------------------------')
        print('----- Conectado con servidor:', self.common, '-----')
        print('----- Conectado con BBDD:', self.dbname, '-----')
        print('----- Numero de registros:', len(data), '-----')
        print('----- Modelo destino:', self.model, '-----')
        print('--------------------------------------------------------------')
        continua = input('<<<<< Continuar con la escritura de datos? (y/n) >>>>> ')
        if continua != 'y': sys.exit()
        print('------------------- Creando Registros ------------------------')
        data_created = []
        n = 0
        for reg in data:
            registro = self.models.execute_kw( self.dbname, self.userID, self.pwd,
                    self.model, 'create', [reg])
            n = n + 1
            print('----- Registro', n, 'creado <<<<<' )
            print(">>>>>", registro, 'Creados <<<<<' )
            data_created.append(registro)
        print('--------------------------------------------------------------')                    
        print("-----", len(data_created), 'Creados -----' )
        print('------------- Creacion de Registros  Finalizada --------------')
