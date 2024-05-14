#!/usr/bin/python3
import sys
import time
import requests

# import copy
from xmlrpc import client
from threading import Thread


# --- Para importar contactos ---
class CreateXMLRCP:

    def __init__(self, url, dbname, user, pwd, model):
        self.url = url
        self.dbname = dbname
        self.user = user
        self.pwd = pwd
        self.model = model
        self.common = ""
        self.userID = ""
        self.models = ""
        self.tamano = 500
        self.start = self.__start()

    # === Test conexion y UserID ===
    def __start(self):
        self.common = client.ServerProxy("{}/xmlrpc/2/common".format(self.url))
        print("==============================================================")
        print("Test: Conexion OK. Server:", self.common)
        self.userID = self.common.authenticate(self.dbname, self.user, self.pwd, {})
        print("COMMON OK. Usuario Autenticado. User ID:", self.userID)
        self.models = client.ServerProxy("{}/xmlrpc/2/object".format(self.url))
        print("MODELS OK. Models:", self.models)
        print("==============================================================")

    # === Division de lista ===
    def __div_list(self, lista, tamanoDiv=None):
        if tamanoDiv is None:
            tamanoDiv = self.tamano
        return [lista[n : n + tamanoDiv] for n in range(0, len(lista), tamanoDiv)]

    # === Lectura de datos ===
    def __mass_read_data(self, div, fields=["name"]):
        # Recibe lista de Ids y utiliza condicion de Includos en "div"
        condicion = [["id", "in", div]]
        # realiza una consulta "search_read" con las Ids de "div"
        data = self.models.execute_kw(
            self.dbname,
            self.userID,
            self.pwd,
            self.model,
            "search_read",
            [condicion],
            {"fields": fields},
        )
        return data

    # === Lectura campos especiales modelo ===
    def __models_props(self):
        fields_list = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )
        selects = []
        many2one = []
        one2many = []
        many2many = []
        fields = []
        for field in fields_list:
            tipo = fields_list[field]["type"]
            match tipo:
                case "selection":
                    selects.append(field)
                case "many2one":
                    many2one.append(field)
                case "one2many":
                    one2many.append(field)
                case "many2many":
                    many2many.append(field)
                case _:
                    fields.append(field)

        return selects, many2one, one2many, many2many, fields

    # ==============================================================
    # === Obtener IDs ===
    def search_ids(self, conditions=[["name", "!=", ""]]):
        data = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "search", [conditions]
        )
        print("==============================================================")
        print("===== Obtener registros OK. Registros obtenidos:", len(data), "=====")
        print("==============================================================")
        return data

    # === Crear Campos de lista ===
    # data: lista de registros a crear
    def create_reg(self, data):
        print("==============================================================")
        print("===== Conectado con servidor:", self.common, "=====")
        print("===== Conectado con BBDD:", self.dbname, "=====")
        print("===== Numero de registros:", len(data), "=====")
        print("===== Modelo destino:", self.model, "=====")
        print("==============================================================")
        continua = input("<<<<< Continuar con la escritura de datos? (y/n) >>>>> ")
        if continua != "y":
            sys.exit()
        print("===================== Creando Registros ======================")
                 
        data_created = []
        n = 0
        for reg in data:
            registro = self.models.execute_kw(
                self.dbname, self.userID, self.pwd, self.model, "create", [reg]
            )
            n = n + 1
            # if n % 100 == 0:
            print(">>>>> Creados", n, "de", len(data), "<<<<<", end="\r")
            data_created.append(registro)
        print("==============================================================")
        print("=====", len(data_created), "Creados =====")
        print("============= Creacion de Registros  Finalizada ==============")

    # Se crean registros en BBDD
    def mass_create_reg(self, data):
        print("==============================================================")
        print("===== Conectado con servidor:", self.common, "=====")
        print("===== Conectado con BBDD:", self.dbname, "=====")
        print("===== Numero de registros:", len(data), "=====")
        print("===== Modelo destino:", self.model, "=====")
        print("==============================================================")
        continua = input("<<<<< Continuar con la escritura de datos? (y/n) >>>>> ")
        if continua != "y":
            sys.exit()
        print("==============================================================")
        print("===================== Creando Registros ======================")
        n = 0
        for regs in data:
            self.models.execute_kw(
                self.dbname, self.userID, self.pwd, self.model, "create", regs
            )
            n += len(regs)
            print(">>>>> Creados", n, "de", len(data), "<<<<<", end='\r')
        print("==============================================================")
        print("===== Initial sample =====")
        print(">>>>>", data[0], "<<<<<")
        print("===== Final sample =====")
        print(">>>>>", data[(len(data)) - 1], "<<<<<")
        print("=====", len(data), "Registros creados =====")
        print("==============================================================")
        print("============= Creacion de Registros  Finalizada ==============")
        print("==============================================================")

    # === Leer Campos de lista de IDs ===
    # ids_list: lista de ids de registros a leer
    # field_list: lista de campos a obtener de cada registro
    def read_data(self, ids_list, field_list=["name"]):
        print("==============================================================")
        print("===== Obteniedo datos de lista =====")
        data = []
        n = 0
        l_select, l_many2one, l_one2many, l_many2many, l_field = self.__models_props()

        # Lectura de registros por id
        for id in ids_list:
            item = self.models.execute_kw(
                self.dbname,
                self.userID,
                self.pwd,
                self.model,
                "read",
                [[id], field_list],
            )
            # Read devuelde una lista con 1 diccionario dentro
            # convierto la consulta en un diccionario
            item = item[0]

            # Cambio de valores en campos especiales (selects, many2one, one2many, many2many)
            for key in field_list:
                if (
                    key in l_select
                    and item[key] != False
                    and type(item[key]) == type([])
                ):
                    item[key] = item[key][0]
                if key in l_many2one and item[key] != False:
                    item[key] = item[key][0]
                if key in l_one2many and item[key] != []:
                    l = []
                    for id in item[key]:
                        l.append((4, id))
                    item[key] = l
            data.append(item)
            n = n + 1
            # if n % 100 == 0:
            print(">>>>> Obtenidos", n, "de", len(ids_list), "<<<<<", end="\r")
            if n == 10:
                break
        print("===== Obtener Finalizado =====")
        print("===== Se han obtenido", n, "de", len(ids_list), "Registros =====")
        print("===== Initial sample =====")
        print(">>>>>", data[0], "<<<<<")
        print("===== Final sample =====")
        print(">>>>>", data[n - 1], "<<<<<")
        print("==============================================================")
        return data

    # === Obtener IDs ===
    # === Leer Campos de lista de IDs ===
    # conditions: Establecer condiciones del Search
    # field: lista de campos a obtener de cada registro
    def mass_read_data(self, field_list=["name"], conditions=[["name", "!=", ""]]):
        # buscamos ids para verificar migracion masiva
        ids = self.search_ids(conditions)

        # eliminar campo corrupto-----------------
        id_corrupt = 0
        n = 0
        for id in ids:
            if id == 16376:
                id_corrupt = n
            n += 1
        del ids[id_corrupt]
        # -----------------------------------------

        # divmos la lista de "ids" en una lista de sublistas "div"
        div = self.__div_list(ids)
        if len(ids) >= self.tamano:
            answer = input("<<<<< Continuar con la lectura de registros? (y/n) >>>>> ")
            # # si desea continuar debe seleccionar "y" o finaliza
            if answer != "y":
                sys, exit()
            mass_data = []
            n_reg = 0
            n = 0
            # recorre las sublistas dentro de "div"
            while n < len(div):
                data = self.__mass_read_data(div[n], field_list)
                mass_data = mass_data + data
                n_reg += len(data)
                print(">>>>> Obtenidos", n_reg, "de", len(ids), "<<<<<", end="\r")
                n += 1
                # if n_reg >= 10:
                #     n = len(div)
            # Cambio de valores en campos especiales (selects, many2one, one2many, many2many)
            l_select, l_many2one, l_one2many, l_many2many, l_field = (
                self.__models_props()
            )
            for key in field_list:
                for item in mass_data:
                    if (
                        key in l_select
                        and item[key] != False
                        and type(item[key]) == type([])
                    ):
                        item[key] = item[key][0]
                    if key in l_many2one and item[key] != False:
                        item[key] = item[key][0]
                    if key in l_one2many and item[key] != []:
                        l = []
                        for id in item[key]:
                            l.append((4, id))
                        item[key] = l
            print("===== Obtener Finalizado =====")
            print("===== Se han obtenido", n_reg, "de", len(ids), "Registros =====")
            print("==============================================================")
            print("===== Initial sample =====")
            print(">>>>>", data[0], "<<<<<")
            print("==============================================================")
            print("===== Final sample =====")
            print(">>>>>", mass_data[(len(mass_data)) - 1], "<<<<<")
            print("==============================================================")
            return mass_data
        else:
            data = self.__mass_read_data(div[0], field_list)
            print("===== Obtener Finalizado -----")
            print(
                "===== Se han obtenido", len(data), "de", len(data), "Registros ====="
            )
            print("===== Initial sample =====")
            print(">>>>>", data[0], "<<<<<")
            print("===== Final sample =====")
            print(">>>>>", len(data), "<<<<<")
            print("==============================================================")
            return data

    # === Update keys registros Migracion ===
    def update_data_keys(self, data_list, old_key, new_key):

        # try:
        #     sample = copy.deepcopy(data_list[0])
        #     # print(sample)
        # except Exception as e:
        #     print(e, " |||| ", str(data_list))

        # Copiamos la posicion 0 sin modificar origen
        sample = data_list[0].copy()
        # Cambia el valor de la key en la muestra
        sample[new_key] = sample.pop(old_key)

        print("==============================================================")
        print(f"===== Actualizacion de key '{old_key}' por '{new_key}' =====")
        print("===== Se han cargado", len(data_list), "registros =====")
        print("==============================================================")
        print("===== Initial sample =====")
        print(">>>>>", data_list[0], "<<<<<")
        print("==============================================================")
        print("===== Final sample =====")
        print(">>>>>", sample, "<<<<<")
        print("==============================================================")
        start_up = input("<<<<< Actualizar todos los registros? (y/n) >>>>> ")
        if start_up != "y":
            sys.exit()
        n = 0
        print(
            "===== Actualizando",
            old_key,
            "por",
            new_key,
            "en",
            len(data_list),
            " =====",
        )
        # Recorro diccionario
        for data in data_list:
            # Cambia los valores de la key
            # print(data[0])
            data[new_key] = data.pop(old_key)
            n += 1
        print("==============================================================")
        print("===== Update keys Finalizado =====")
        print("===== Se han modificado", n, "de", len(data_list), "Registros =====")
        print("==============================================================")
        print("===== Initial sample =====")
        print(">>>>>", data_list[0], "<<<<<")
        print("==============================================================")
        print("===== Final sample =====")
        print(">>>>>", data_list[(len(data_list)) - 1], "<<<<<")
        print("==============================================================")
        return data_list

    def update_reg_values(self, data_list, old_model):
        pass

    # === Devuelve campos usados con cantidad de usos ===
    # === Devuelve campos sin uso en el modelo ===
    def models_use(self, conditions=[["name", "!=", ""]], field_ignore=[]):
        # Obtener datos modelo
        # hago un search_read con todos los campos del modelo
        fields_list = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )

        # Iteramos las key y la guardamos como lista
        fields_name = list(fields_list.keys())
        # fields_name = fields_name[:10]
        print("--------------------------------------------------------------")
        print("----- Se han Obtenido", len(fields_name), "campos -----")
        print("--------------------------------------------------------------")

        # Busqueda campos especiales || Blacklist
        fields_error = ["email_formatted"]
        # for field in fields_name :
        # Buscando campos obligatorios
        # if fields_list[field]['required'] : fields_req.append(field)
        # Buscamos campos readonly
        # if fields_list[field]['readonly'] : fields_RO.append(field)
        fields_BL = field_ignore + fields_error
        # Eliminar campos especiales de
        fields_name_BL = [x for x in fields_name if x not in fields_BL]
        # ----------------------------------------

        # buscamos ids para verificar migracion masiva
        ids = self.search_ids(conditions)
        # eliminar campo corrupto-----------------
        id_corrupt = 0
        n = 0
        for id in ids:
            if id == 16376:
                id_corrupt = n
            n += 1
        del ids[id_corrupt]
        # -----------------------------------------
        # Incremento tamano de lotes para lectura de a un campo
        tamano = self.tamano * 5
        div = self.__div_list(ids, tamano)

        # listas de uso
        field_use = []
        field_no_use = []
        n_fields = 1

        # Iteracion de Campos de modelo
        for field in fields_name_BL:
            key_use = []
            n_use = 0
            n_reg = 0
            n = 0
            mass_data = []
            default = ""
            print("--------------------------------------------------------------")
            print(
                "----- Obteniendo datos del campo",
                field,
                ". ",
                f"{n_fields}/{len(fields_name_BL)+1}",
                "-----",
            )
            n_fields += 1
            # Iteracion de Ids obtenidas por campos
            while n < len(div):
                n_use = 0
                n_reg += len(div[n])
                data = self.__mass_read_data(div[n], [field])
                print(
                    ">>>>> Obtenidos",
                    n_reg,
                    "registros de",
                    len(ids),
                    ". <<<<<",
                    end="\r",
                )
                mass_data = mass_data + data
                n += 1
                if n_reg == 500:
                    n = len(div)
            # Verifica Uso del Campo
            for data in mass_data:
                if "change_default" in fields_list.get(field, {}):
                    default = fields_list[field]["change_default"]
                if (
                    (data[field] == default)
                    or (data[field] == "")
                    or (data[field] == [])
                ):
                    pass
                else:
                    n_use += 1
            # Agrego Campo a la lista de Uso
            if n_use != 0:
                field_use.append({field: n_use})
            else:
                field_no_use.append(field)
        print("--------------------------------------------------------------")

        # Ordena los datos por key y los imprime
        field_use.sort(key=lambda x: next(iter(x.keys())), reverse=False)
        for field in field_use:
            key = next(iter(field))
            valor = next(iter(field.values()))
            print(">>>>>", f"{key}: {valor}")
        print("--------------------------------------------------------------")
        print("----- Campos utilizado por modelo", len(field_use), "-----")
        print("--------------------------------------------------------------")
        print(">>>> Lista de campos sin usar:", field_no_use)
        print("--------------------------------------------------------------")

    # === Compara Campos de Origen y Destino ===
    # Devuelve keys encontradas en BBDD destino
    # Devuelve keys no encontradas en BBDD
    # Devuelve keys restantes en BBDD destino
    def models_compare_fields(self, field_list_origen):
        fields_list = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )
        fields_names = []
        fields_find = []
        fields_no_find = []
        fields_rest = []
        for field in fields_list:
            fields_names.append(field)

        fields_find = [x for x in fields_names if x in field_list_origen]
        fields_no_find = [x for x in field_list_origen if x not in fields_names]
        fields_rest = [x for x in fields_names if x not in field_list_origen]

        fields_find.sort()
        fields_no_find.sort()
        fields_rest.sort()

        print("--------------------------------------------------------------")
        print(">>>> Lista de campos coincidentes:", fields_find)
        print(">>>> Campos coincidentes:", len(fields_find))
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print(">>>> Lista de campos sin coincidencias:", fields_no_find)
        print(">>>> Campos sin coincidencias:", len(fields_no_find))
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print(">>>> Lista de campos destino:", fields_rest)
        print(">>>> Campos destino:", len(fields_rest))
        print("--------------------------------------------------------------")

        # print(fields_list['write_date'])

    # Devuelve campos especiales
    def models_props(self):
        selects, many2one, one2many, many2many, fields = self.__models_props()
        selects.sort()
        many2many.sort()
        one2many.sort()
        many2many.sort()
        fields.sort()
        ne = len(selects) + len(many2one) + len(one2many) + len(many2many)
        print("==============================================================")
        print(f"===== Campos S/C =====")
        print("==============================================================")
        print(f">>>>> Campos Campos S/C {len(fields)} <<<<<")
        print(f" {fields}")
        print("==============================================================")
        print(f"===== Campos especiales {ne} =====")
        print("==============================================================")
        print(f">>>>> Campos selects {len(selects)} <<<<<")
        print(f" {selects}")
        print("==============================================================")
        print(f">>>>> Campos many2one {len(many2one)} <<<<<")
        print(f" {many2one}")
        print("==============================================================")
        print(f">>>>> Campos one2many {len(one2many)} <<<<<")
        print(f" {one2many}")
        print("==============================================================")
        print(f">>>>> Campos many2many {len(many2many)} <<<<<")
        print(f" {many2many}")
        print("==============================================================")
