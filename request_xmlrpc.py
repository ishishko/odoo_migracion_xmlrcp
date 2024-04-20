#!/usr/bin/python3
#para importar contactos solo

from xmlrpc import client


class RequestXMLRCP:
    def __init__(self, dbname, user, pwd, url='https://geminis.ntsystemwork.com.ar/'):
        self.dbname = dbname
        self.user = user
        self.pwd = pwd
        self.url = url
        self.common = client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(dbname,user,pwd,{})

    def __crud(self, model:str='res.partner', action_type:str='read', fields=['id'], conditions=[])->list:
        models = client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        data = models.execute_kw(self.dbname, self.uid, self.pwd, model, action_type, [
        [1], fields])
        return data

    def search(self, model='account.invoice', conditions=[['display_name', '!=', '']]):
        data = self.common.execute_kw(self.dbname, self.uid, self.pwd, 'account.invoice', 'search', 
        [conditions])
        return data

    def read(self, model:str='res.partner', fields:list=['id']):
        self.__crud(model, 'read', fields)


 

if __name__ == '__main__':
    dbname = 'geminis'
    user = 'admin'
    pwd = 'gemi19nis'
    r = RequestXMLRCP(dbname,user,pwd)
    print(r.search())

