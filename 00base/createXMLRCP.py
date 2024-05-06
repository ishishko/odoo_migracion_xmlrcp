#!/usr/bin/python3
import sys
import time
import requests
from xmlrpc import client
from threading import Thread


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
        self.tamano = 1000
        self.start = self.__start()

    # --- Test conexion y UserID ---
    def __start(self) :
        self.common = client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        print('--------------------------------------------------------------')
        print ('Test: Conexion OK. Server:', self.common)
        self.userID = self.common.authenticate(self.dbname,self.user,self.pwd,{})
        print ("COMMON OK. Usuario Autenticado. User ID:", self.userID)
        self.models = client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        print ('MODELS OK. Models:', self.models)
        print('--------------------------------------------------------------')
    # --- Division de lista ----
    def __div_list(self, lista, tamanoDiv = None):
        if tamanoDiv is None:
            tamanoDiv = self.tamano
        return [lista[n:n+tamanoDiv] for n in range(0, len(lista), tamanoDiv)]
    # --- Lectura de datos ---
    def __mass_read_data(self, div, fields=['name'] ) :
        # Recibe lista de Ids y utiliza condicion de Includos en "div"
        condicion = [['id' , 'in' , div]]
        # realiza una consulta "search_read" con las Ids de "div" 
        data = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model,
            'search_read', [condicion], {'fields': fields })
        return data


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

        #eliminar campo corrupto-----------------
        id_corrupt = 0
        n = 0
        for id in ids:
            if id == 16376 : id_corrupt = n
            n += 1
        del ids[id_corrupt]
        #-----------------------------------------

        # divmos la lista de "ids" en una lista de sublistas "div"
        div = self.__div_list(ids)
        if len(ids)>= self.tamano :
            answer = input('<<<<< Continuar con la lectura de registros? (y/n) >>>>> ')
            # # si desea continuar debe seleccionar "y" o finaliza
            if answer != 'y' : sys,exit()
            mass_data = []
            n_reg =0
            n = 0
            # recorre las sublistas dentro de "div"
            while n < len(div):
                data = self.__mass_read_data( div[n], fields )
                mass_data = mass_data + data
                n_reg += len(data)
                print('>>>>> Obtenidos',n_reg, 'de', len(ids),'<<<<<')
                n += 1
                # if n_reg >= 1000 : n = len(div)

            print('----- Obtener Finalizado -----')
            print('----- Se han obtenido', n_reg , 'de' , len(ids),'Registros -----')
            print('--------------------------------------------------------------')
            print('----- Initial sample -----')
            print('>>>>>', data[0], '<<<<<')
            print('--------------------------------------------------------------')
            print('----- Final sample -----')
            print('>>>>>', mass_data[(len(mass_data))-1], '<<<<<')
            print('--------------------------------------------------------------')
            return mass_data
        else :
            data = self.__mass_read_data(div[0], fields )
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
        print('--------------------------------------------------------------')
        print('------------------- Creando Registros ------------------------')
        div = self.__div_list(data)
        n = 0
        for regs in div :
            self.models.execute_kw( self.dbname, self.userID, self.pwd,
                    self.model, 'create', regs)
            n += len(regs)
            print('>>>>> Creados',n, 'de', len(data),'<<<<<')        
        print('--------------------------------------------------------------')
        print('----- Initial sample -----')
        print('>>>>>', data[0], '<<<<<')
        print('----- Final sample -----')
        print('>>>>>', data[(len(data))-1], '<<<<<')
        print("-----", len(data), 'Registros creados -----' )
        print('--------------------------------------------------------------')
        print('------------- Creacion de Registros  Finalizada --------------')
        print('--------------------------------------------------------------')

    # --- Update datos Migracion ---
    def update_reg_keys(self, data_list ,old_key, new_key ) :
        # Copiamos la posicion 0 sin modificar origen
        sample = data_list[0].copy()
        # Cambia el valor de la key en la muestra
        sample[new_key] = sample.pop(old_key)
        print('--------------------------------------------------------------')
        print('----- Se han cargado', len(data_list) ,'registros -----')
        print('--------------------------------------------------------------')
        print('----- Initial sample -----')
        print('>>>>>', data_list[0], '<<<<<')
        print('--------------------------------------------------------------')
        print('----- Final sample -----')
        print('>>>>>', sample, '<<<<<')
        print('--------------------------------------------------------------')
        start_up = input('<<<<< Actualizar todos los registros? (y/n) >>>>> ')
        if start_up != 'y' : sys.exit()
        n = 0
        print('----- Actualizando', old_key, 'por', new_key, 'en', len(data_list) ,' -----')
        # Recorro diccionario
        for data in data_list :
            # Cambia los valores de la key
            data[new_key] = data.pop(old_key)
            n += 1
        print('--------------------------------------------------------------')
        print('----- Update keys Finalizado -----')
        print('----- Se han modificado', n , 'de' , len(data_list),'Registros -----')
        print('--------------------------------------------------------------')
        print('----- Initial sample -----')
        print('>>>>>', data_list[0], '<<<<<')
        print('--------------------------------------------------------------')
        print('----- Final sample -----')
        print('>>>>>', data_list[(len(data_list))-1], '<<<<<')
        print('--------------------------------------------------------------')
        return data_list
            
    def update_reg_values(self, data_list, old_model) :
        pass
    
    def models_use(self, conditions = [['name', '!=' ,'']]) :
        # Obtener datos modelo
        # hago un search_read con todos los campos del modelo
        fields_list = self.models.execute_kw(self.dbname, self.userID, self.pwd,
                      self.model, 'fields_get', [[]])
        
        # Creo un diccionario con cada campo
        fields_name = []

        # print(fields_list['name'])
        for field in fields_list :
            fields_name.append(field)    
        print('--------------------------------------------------------------')
        print('----- Se han Obtenido', len(fields_name), 'campos -----')
        print('--------------------------------------------------------------')
        
        # buscamos ids para verificar migracion masiva
        ids = self.search_ids(conditions)
        #eliminar campo corrupto-----------------
        id_corrupt = 0
        n = 0
        for id in ids:
            if id == 16376 : id_corrupt = n
            n += 1
        del ids[id_corrupt]

        # Incremento tamano de lotes para lectura de a un campo
        tamano = self.tamano * 5
        div = self.__div_list(ids, tamano)

        # # Obtengo todos los registros COMPLETOS de la BBDD
        
        # for field in fields_name:
        #     print(field)
        #     print('--------------------------------------------------------------')
        #     print('----- Obteniedo los valores de', field, ' -----')
        #     print('--------------------------------------------------------------')
        #     data = self.mass_read_data([['name', '!=', '']],field)
        #     print('--------------------------------------------------------------')
        #     print('----- Se han Obtenido los valores de', field, ' -----')
        #     print('--------------------------------------------------------------')
        # print(len(fields_name))
        # n = 0
        # while n < 4 :
        #     print(fields_list["name"])
        #     n += 1
        
        # print(fields_name)
        

