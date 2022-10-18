from .models import *


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        
        if model == client:
            return 'mssql_railways'
        elif model == wagons:
            return 'mssql_railways'
        elif model == station:
            return 'mssql_railways'
        elif model == cargo:
            return 'mssql_railways'
        elif model == coming:
            return 'mssql_railways'
        elif model == sort:
            return 'mssql_railways'
        elif model == depart:
            return 'mssql_railways'
            
        return None

    #def db_for_write(self, model, **hints):
    #    if model == client:
    #        return 'mssql_railways'
     #   return None
  

    