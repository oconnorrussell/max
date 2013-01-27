from    src.properties import propManager
import  sys
from    src.logger  import  logger

class conn():

    def __init__(self):

        self.pm =   propManager.propertyManager()
        
        self.user    =   self.pm.get('DB_USER')
        self.passwd  =   self.pm.get('DB_PWD')

    def connect(self):
        pass
        
    def cursor(self):
        #    assumes connection made
        return  self.conn.cursor()
        