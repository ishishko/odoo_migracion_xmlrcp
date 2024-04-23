#!/usr/bin/python3
import sys
import time
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

    # --- Test conexion y UserID ---
    def __start(self) :
        self.common = client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        print('--------------------------------------------------------------')
        print ('Test: Conexion OK. Server:', self.common)
        self.userID = self.common.authenticate(self.dbname,self.user,self.pwd,{})
        print ("COMMON OK. Usuario Autenticado. User ID:", self.userID)
        self.models = models = client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        print ('MODELS OK. Models:', self.models)
        print('--------------------------------------------------------------')
    def __div_list(self, lista, tamano=100) :
        return [lista[n:n+tamano] for n in range(0,len(lista),tamano)]
    # --- Obtener IDs ---
    def search_ids(self, conditions=[['name', '!=', '']]) :
        data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, 'search', 
        [conditions])
        print("Obtener registros OK. Registros obtenidos:", len(data))
        return data
    
    # --- Leer Campos de lista de IDs ---
    # ids_list: lista de ids de registros a leer
    # field_list: lista de campos a obtener de cada registro
    def read_data(self, ids_list, field_list = ['name'] ) :
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
            if n == 10: break
        print('----- Obtener Finalizado -----')
        print('----- Se han obtenido', n , 'de' , len(ids_list),'Registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', data[n-1], '<<<<<')
        print('--------------------------------------------------------------')
        return data
    
    # --- Obtener IDs ---
    # --- Leer Campos de lista de IDs ---
    # ids_list: lista de ids de registros a leer
    # field_list: lista de campos a obtener de cada registro
    def search_read_data( self, conditions=[['name', '!=', '']], fields=['name'] ):
        print()
        ids = self.search_ids()
        input('<<<<< Continuar con la escritura de datos? (y/n) >>>>> ')

        if len(ids) > 1000 :
            input('<<<<< Continuar con la escritura de datos? (y/n) >>>>> ')
        data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
               'search_read', [conditions], {'fields': fields, 'limit': 1000 })
        print('----- Obtener Finalizado -----')
        print('----- Se han obtenido', len(data) , 'de' , len(data),'Registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', data[(len(data))-1], '<<<<<')
        print('--------------------------------------------------------------')
        return data

    # --- Crear Campos de lista ---
    # data: lista de registros a crear
    def create_reg(self, data) :
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
            if n % 100 == 0: print('>>>>> Creados',n, 'de', len(data))
            data_created.append(registro)
        print('--------------------------------------------------------------')                    
        print("-----", len(data_created), 'Creados -----' )
        print('------------- Creacion de Registros  Finalizada --------------')

    # --- Obtener IDs ---
    # --- Leer Campos de lista de IDs ---
    # ids_list: lista de ids de registros a leer
    # field_list: lista de campos a obtener de cada registro
    def mass_read_data( self, conditions=[['name', '!=', '']], fields=['name'] ):
        print()
        ids = self.search_ids(conditions)
        div = self.__div_list(ids)
        if len(ids)>= 1000 :
            answer = input('<<<<< Continuar con la lectura de registros? (y/n) >>>>> ')
            if answer != 'y' : sys,exit()
            mass_data = []
            ni = 0
            nf = 1000
            n = 0
            while ni <= len(ids):
                condicion = [['id' , 'in' , div[n]]]
                data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
                    'search_read', [condicion], {'fields': fields , 'offset':ni,'limit':nf })
                mass_data = mass_data + data
                print('>>>>> Obtenidos',nf, 'de', len(ids),'<<<<<')
                nf += len(data) - ni
                ni += 1000
                n += 1
            print('----- Obtener Finalizado -----')
            print('----- Se han obtenido', nf , 'de' , len(mass_data),'Registros -----')
            print('----- Initial sample -----')
            print('>>>>>', data[0], '<<<<<')
            print('----- Final sample -----')
            print('>>>>>', data[(len(data))-1], '<<<<<')
            print('--------------------------------------------------------------')
        else :
            div = self.__div_list(ids)
            condicion = [['id' , 'in' , div[0]]]
            data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
               'search_read', [conditions], {'fields': fields})
        

        print('----- Obtener Finalizado -----')
        print('----- Se han obtenido', len(data) , 'de' , len(data),'Registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', len(data), '<<<<<')
        print('--------------------------------------------------------------')
        return data

    def __mass_read_data(self):
        pass
    # --- Update datos Migracion ---
    #
    # def update_reg_country(self, conditions ) :
    #     data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, 'search', 
    #     [conditions])

