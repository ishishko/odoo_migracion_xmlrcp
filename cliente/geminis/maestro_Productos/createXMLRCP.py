#!/usr/bin/python3
import sys
import time
import requests
import re
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
        self.tamano = 100
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

    def __levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.__levenshtein_distance(s2, s1)

        # Si una de las cadenas está vacía, la distancia es la longitud de la otra
        if len(s2) == 0:
            return len(s1)

        # Crear una matriz de la longitud de la segunda cadena más uno
        previous_row = range(len(s2) + 1)

        # Iterar sobre cada caracter de la primera cadena
        for i, c1 in enumerate(s1):
            current_row = [i + 1]

            # Iterar sobre cada caracter de la segunda cadena
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))

            previous_row = current_row
            return previous_row[-1]
    
    def __guardar_en_txt(self, datos, nombre_archivo):
        """
        Guarda los datos proporcionados en un archivo de texto.

        :param datos: Cadena de texto o lista de líneas a guardar en el archivo.
        :param nombre_archivo: Nombre del archivo donde se guardarán los datos.
        """
        
        texto = '\n'.join(map(str, datos))

        with open(nombre_archivo, 'w') as archivo:
            # Si los datos son una lista, unirlos con saltos de línea
            if isinstance(texto, list):
                archivo.write('\n'.join(texto))
            else:
                archivo.write(texto)
        print(f"Datos guardados en {nombre_archivo}")

    # ==============================================================
    # === Obtener IDs ===
    def search_ids(self, conditions=[["id", "!=", 0]]):
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
            try:
                self.models.execute_kw(
                    self.dbname, self.userID, self.pwd, self.model, "create", [regs]
                )
                n += 1
            except Exception as e:
                print("==============================================================")
                print(f"146 - {regs}")
                print("==============================================================")
                print(f">>>>> {e}")
                print("==============================================================")
                continua = input(
                    "<<<<< Continuar con la escritura de datos? (y/n) >>>>> "
                )
                if continua != "y":
                    sys.exit()
                continue
            # print(f">>>>> {regs}")
            print(">>>>> Creados", n, "de", len(data), "<<<<<", end="\r")
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
    def read_data(self, ids_list, field_list=["id"]):
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
                # select field type
                if (
                    key in l_select
                    and item[key] != False
                    and type(item[key]) == type([])
                ):
                    item[key] = item[key][0]

                # m2o field type
                if key in l_many2one and item[key] != False:
                    item[key] = item[key][0]

                # m2m field type
                if key in l_many2many and item[key] != False:
                    if item[key] != []:
                        item[key] = item[key]

                # # o2m field type
                # if key in l_one2many and item[key] != []:
                #     l = []
                #     for id in item[key]:
                #         l.append((0, 0, {"id": id}))
                #     try:
                #         item[key] = l
                #     except Exception as e:
                #         print("203 - ", e)
                #         item[key] = []
                #         continue
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
    def mass_read_data(self, field_list=["id"], conditions=[["id", "!=", 0]]):
        # buscamos ids para verificar migracion masiva
        ids = self.search_ids(conditions)

        # # eliminar campo corrupto-----------------
        # id_corrupt = 0
        # n = 0
        # if len(ids) != 0:
        #     for id in ids:
        #         if id == 16376:
        #             id_corrupt = n
        #         n += 1
        #     del ids[id_corrupt]
        # # -----------------------------------------

        if len(ids) >= self.tamano:
            answer = input("<<<<< Continuar con la lectura de registros? (y/n) >>>>> ")
            # si desea continuar debe seleccionar "y" o finaliza
            if answer != "y":
                sys, exit()

            # divimos la lista de "ids" en una lista de sublistas "div"
            div = self.__div_list(ids)

            # declaramos varibles para  while
            mass_data = []
            n_reg = 0
            n = 0

            # recorre las sublistas dentro de "div"
            while n < len(div):
                print(f">>>>> Obtenidos {n_reg} de {len(ids)} ", end="\r")
                data = self.__mass_read_data(div[n], field_list)
                mass_data = mass_data + data
                n_reg += len(data)
                n += 1

            # Cambio de valores en campos especiales (selects, many2one, one2many, many2many)
            l_select, l_many2one, l_one2many, l_many2many, l_field = (
                self.__models_props()
            )
            for key in field_list:
                for item in mass_data:
                    # select field type
                    if (
                        key in l_select
                        and item[key] != False
                        and type(item[key]) == type([])
                    ):
                        item[key] = item[key][0]

                    # m2o field type
                    if key in l_many2one and item[key] != False:
                        item[key] = item[key][0]

                    # m2m field type
                    if key in l_many2many and item[key] != False:
                        if item[key] != []:
                            item[key] = item[key]

                    # # o2m field type
                    # if key in l_one2many and item[key] != []:
                    #     l = []
                    #     for id in item[key]:
                    #         l.append((0, 0, {"id": id}))
                    #     try:
                    #         item[key] = l
                    #     except Exception as e:
                    #         print("203 - ", e)
                    #         item[key] = []
                    #         continue

            # Imprime info de la lectura
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
            if len(ids) != 0:
                data = self.__mass_read_data(ids, field_list)
                print("===== Obtener Finalizado -----")
                print(
                    "===== Se han obtenido",
                    len(data),
                    "de",
                    len(data),
                    "Registros =====",
                )
                print("===== Initial sample =====")
                print(">>>>>", data[0], "<<<<<")
                print("===== Final sample =====")
                print(">>>>>", data[len(data) - 1], "<<<<<")
                print("==============================================================")
                return data
            else:
                print("==============================================================")
                print("================= Consulta sin coincidencias =================")
                print("==============================================================")

    # === Update keys registros Migracion ===
    def change_data_keys(self, data_list, old_key, new_key):

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
            f'===== Actualizando "{old_key}" por "{new_key}" en {len(data_list)} ====='
        )

        # Itero diccionario
        for data in data_list:
            # Cambia los valores de la key
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

    def change_data_values(self, data_list, field_key, field_value):
        for i in range(len(data_list)):
            data_list[i][field_key] = field_value
        return data_list

    # === Devuelve campos usados con cantidad de usos ===
    # === Separa los campos por tipo para migracion ordenada ===
    # === Devuelve campos sin uso en el modelo ===
    def models_use(self, field_ignore=[], conditions=[["id", "!=", 0]]):
        # Obtener datos modelo
        # hago un fields_get de todos los campos del modelo
        fields_list = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )

        # Iteramos las key y la guardamos como lista
        fields_name = list(fields_list.keys())
        # fields_name = fields_name[:10]
        
        # Busqueda campos especiales || Blacklist
        fields_error = []
        fields_BL = field_ignore + fields_error
        # Eliminar campos especiales de
        fields_name_BL = [x for x in fields_name if x not in fields_BL]
        print("==============================================================")
        print(f"===== Se han Obtenido {len(fields_name_BL)} campos =====")
        print("==============================================================")
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
        tamano = self.tamano * 4
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
            print("==============================================================")
            print(
                f'===== Obteniendo datos del campo "{field}". {n_fields}/{len(fields_name_BL)} ====='
            )
            n_fields += 1
            # Iteracion de Ids obtenidas por campos
            while n < len(div):
                n_use = 0
                print(
                    f">>>>> Obtenidos {n_reg} registros de {len(ids)}. <<<<<", end="\r"
                )
                n_reg += len(div[n])
                data = self.__mass_read_data(div[n], [field])
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
                    or (data[field] == {})
                ):
                    pass
                else:
                    n_use += 1
            # Agrego Campo a la lista de Uso
            if n_use != 0:
                field_use.append({field: n_use})
            else:
                field_no_use.append(field)
        print("==============================================================")

        # Ordena los datos por key y los imprime
        field_use.sort(key=lambda x: next(iter(x.keys())), reverse=False)
        field_no_use.sort()
        keys_field_use = []
        for field in field_use:
            key = next(iter(field))
            valor = next(iter(field.values()))
            keys_field_use.append(key)
            print(">>>>>", f"{key}: {valor}")
        print("==============================================================")
        print(f"===== Campos utilizado por modelo {len(field_use)} :")
        print(f"{keys_field_use}")
        print("==============================================================")
        print(f">>>>> Lista de campos sin usar {len(field_no_use)} :")
        print(f">>>>> {field_no_use}")
        print("==============================================================")

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

        print("==============================================================")
        print(f"===== Campos coincidentes: {len(fields_find)} =====")
        print("===== Lista de campos coincidentes:")
        print(f">>>>> {fields_find}")
        print("==============================================================")
        print(f"===== Campos sin coincidencias:, {len(fields_no_find)}")
        print("===== Lista de campos sin coincidencias:")
        print(f">>>>> {fields_no_find}")
        print("==============================================================")
        print(f"===== Campos destino:, {len(fields_rest)} =====")
        print("===== Lista de campos destino:")
        print(f">>>>> {fields_rest}")
        print("==============================================================")

        # print(fields_list['write_date'])

    # === Devuelve campos por tipo ===
    def models_fields_types(self, fields_list=[]):
        # Separo los campos por tipo
        selects, many2one, one2many, many2many, fields = self.__models_props()
        # Ordeno las listas de campos
        selects.sort()
        many2many.sort()
        one2many.sort()
        many2many.sort()
        fields.sort()
        # si se pasa una lista especifica verifico que esten en la misma por tipo
        if fields_list != []:
            selects = [x for x in selects if x in fields_list]
            many2many = [x for x in many2many if x in fields_list]
            one2many = [x for x in one2many if x in fields_list]
            many2many = [x for x in many2many if x in fields_list]
            fields = [x for x in fields if x in fields_list]
        ne = len(selects) + len(many2one) + len(one2many) + len(many2many)
        print("==============================================================")
        print(f'===== Modelo "{self.model}" =====')
        print(f"===== Campos S/C {len(fields)} =====")
        print("==============================================================")
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

    # === Devuelve informacion tecnica de los campos deseados ===
    def models_fields_props(self, fields_list=[]):
        print("==============================================================")
        if fields_list == []:
            print("============ Debe ingresar una lista de campos ===============")
            print("==============================================================")
            sys, exit()

        fields_props = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )

        fields_list.sort()

        for name in fields_list:
            for field in fields_props.items():
                if name == field[0]:
                    props_campo = {k: field[1][k] for k in sorted(field[1])}
                    print(f'===== Props campo "{field[0]}" =====')
                    print(f">>>>> {props_campo} ")
                    print(
                        "=============================================================="
                    )

    # === Lectura de Campos del modelo ===
    def models_status(self):
        fields_props = self.models.execute_kw(
            self.dbname, self.userID, self.pwd, self.model, "fields_get", [[]]
        )

        for field in fields_props.items():
            print("==============================================================")
            print(f'===== Campo "{field[0]}" =====')
            print(f">>>>> {field[1]}")

    # === Update de campos del modelo ===
    def models_update(self, data_origen, data_destino):
        encontrados = []
        # corta = 0
        # larga = 0
        # media = 0
        
        ids_o = set()
        ids_d = set()
        
        for data_d in data_destino:
            for data_o in data_origen:
                destino = re.sub(r"[^a-zA-Z0-9]", "", data_d["name"])
                origen = re.sub(r"[^a-zA-Z0-9]", "", data_o["name"])
                
                # 394 resultado con ids repetidas
                # if destino.lower() == origen.lower():
                #     if data_o['image_1920'] or data_o['image_1024'] or data_o['image_128']:
                #         encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                #         print(f'encontrado: {data_d["name"]} --- {data_o["name"]}')
                            # upd = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, "write", [[data_d['id']], {'image_1920': data_o['image_1920'], 'image_1024': data_o['image_1024'], 'image_128': data_o['image_128']}])
                
                # 259 resultado sin ids repetidas
                if (destino.lower() == origen.lower()) and (data_o['id'] not in ids_o) and (data_d['id'] not in ids_d):
                    if data_o['image'] or data_o['image_medium'] or data_o['image_small']:
                        encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                        ids_d.add(data_d['id'])
                        ids_o.add(data_o['id'])
                        print(f'encontrado: {data_d["name"]} --- {data_o["name"]}')
                        upd = self.models.execute_kw(self.dbname, self.userID, self.pwd, self.model, "write", [[data_d['id']], {'image_1920': data_o['image'], 'image_1024': data_o['image_medium'], 'image_128': data_o['image_small']}])
                

                # if (len(destino.lower()) <= 7 or len(origen.lower()) <= 7) and len(destino.lower()) - len(origen.lower()) <= 4:
                #     if self.__levenshtein_distance(destino.lower(), origen.lower()) < 3:
                #         encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                #         corta += 1
                # elif (len(destino.lower()) <= 20 or len(origen.lower()) <= 20) and len(destino.lower()) - len(origen.lower()) <= 7:
                #     if self.__levenshtein_distance(destino.lower(), origen.lower()) < 3:
                #         encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                #         media += 1
                # else:
                #     if self.__levenshtein_distance(destino.lower(), origen.lower()) < 3:
                #         encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                #         larga += 1


                # if (self.__levenshtein_distance(destino.lower(), origen.lower()) < 4) and abs(len(destino.lower())-len(origen.lower())) < 3:
                #     if data_d['id'] not in ids_d :
                #         encontrados.append({"destino": data_d['name'], "origen": data_o['name']})
                #         print(f'encontrado: {data_d["name"]} --- {data_o["name"]}')
                #         ids_d.add(data_d['id'])
                #         ids_o.add(data_o['id'])
                    

        # print(encontrados)
        print(len(encontrados))
        self.__guardar_en_txt(encontrados, 'resultados4.txt')
        
        

