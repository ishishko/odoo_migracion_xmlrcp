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
    # --- Division de lista ----
    def __div_list(self, lista, tamano=100) :
        return [lista[n:n+tamano] for n in range(0,len(lista),tamano)]
    
    # --- Obtener IDs ---
    def search_ids(self, conditions=[['name', '!=', '']]) :
        data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, 'search', 
        [conditions])
        print('--------------------------------------------------------------')
        print("----- Obtener registros OK. Registros obtenidos:", len(data),'-----')
        print('--------------------------------------------------------------')
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
    # conditions: Establecer condiciones del Search
    # field: lista de campos a obtener de cada registro
    def mass_read_data( self, conditions=[['name', '!=', '']], fields=['name'] ):
        # buscamos ids para verificar migracion masiva
        ids = self.search_ids(conditions)
        # divmos la lista de "ids" en una lista de sublistas "div"
        div = self.__div_list(ids)
        if len(ids)>= 100 :
            answer = input('<<<<< Continuar con la lectura de registros? (y/n) >>>>> ')
            # si desea continuar debe seleccionar "y" o finaliza
            if answer != 'y' : sys,exit()
            mass_data = []
            n_reg =0
            n = 0
            # recorre las sublistas dentro de "div"
            while n < len(div):
                condicion = [['id' , 'in' , div[n]]]
                # realiza una consulta "search_read" para cada sublista
                data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
                    'search_read', [condicion], {'fields': fields })
                # agrega los registro de "data" a la lista final "mass_data"
                mass_data = mass_data + data
                n_reg += len(data)
                print('>>>>> Obtenidos',n_reg, 'de', len(ids),'<<<<<')
                n += 1
                if n_reg >= 1000 : n = len(div)

            print('----- Obtener Finalizado -----')
            print('----- Se han obtenido', n_reg , 'de' , len(mass_data),'Registros -----')
            print('----- Initial sample -----')
            print('>>>>>', data[0], '<<<<<')
            print('----- Final sample -----')
            print('>>>>>', mass_data[(len(mass_data))-1], '<<<<<')
            print('--------------------------------------------------------------')
            return mass_data
        else :
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

    def mass_create_reg(self, data) :
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

    # --- Update datos Migracion ---
    def update_reg_keys(self, data_list ,old_key, new_key ) :
        sample = data_list[0].copy()
        sample[new_key] = sample.pop(old_key)
        print('--------------------------------------------------------------')
        print('----- Se han cargado', len(data_list) ,'registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data_list[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', sample, '<<<<<')
        start_up = input('<<<<< Actualizar todos los registros? (y/n) >>>>> ')
        if start_up != 'y' : sys.exit()
        n = 0
        print('----- Actualizando', old_key, 'por', new_key, 'en', len(data_list) ,' -----')
        for data in data_list :
            data[new_key] = data.pop(old_key)
            n += 1
        print('--------------------------------------------------------------')
        print('----- Update keys Finalizado -----')
        print('----- Se han modificado', n , 'de' , len(data_list),'Registros -----')
        print('----- Initial sample -----')
        print('>>>>>', data_list[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', data_list[(len(data_list))-1], '<<<<<')
        print('--------------------------------------------------------------')
        return data_list
            
    def update_reg_values(self, data_list, old_model):
        pass
