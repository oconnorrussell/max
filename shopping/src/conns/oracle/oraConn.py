'''
Created on Jan 6, 2013

@author: RussellR
'''
import MySQLdb
from properties.src import propManager
import sys

class oraConn():

    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.pm =   propManager.propertyManager()
        
        self.host    =   self.pm.get('DB_HOST')
        self.port    =   self.pm.get('DB_PORT')
        self.passwd  =   self.pm.get('DB_PWD')
        self.db      =   self.pm.get('DB_NAME')
        self.user    =   self.pm.get('DB_USER')

    def connect(self):

        #print 'host=' + host + ' ,port = ' + port + ' ,passwd=' + passwd + ' ,db=' + db + ' ,user=' + user
        try:
            self.conn=MySQLdb.connect(host=self.host,port=int(self.port),passwd=self.passwd,db=self.db,user=self.user)
            #self.conn=MySQLdb.connect(host="81.17.241.90",port=3306,passwd="ghtdf567b",db="m48971_shopping",user="m48971_shopping")
        except MySQLdb.Error, e:
              print "Error %d: %s" % (e.args[0], e.args[1])
              sys.exit(1)
        else:
            print 'connected to ' +  self.pm.get('DB_HOST')        


    def cursor(self):
            return  self.conn.cursor()
        