import sys
from logger import logger
import os


class propManager():
    
    def __init__(self):
        propFile = None
        print 'SM_PROP_DIR = ' + str(os.environ.get('SM_PROP_DIR'))
        if os.environ.has_key('SM_PROP_DIR'):
            try:
                propFile = os.environ.get('SM_PROP_DIR') + '\propertyfile.dat'
            except:
                print 'failed to form propFile, aborting.'
                sys.exit()
            else:
                try:
                    print 'attempting to open propertyfile.dat =' + propFile
                    myfile = open(propFile, 'r')
                except:
                    logger.err("failed to open propertyfile = " + propFile + '. aborting')
                    sys.exit()
                else:
                    self.properties = {}
                    property = {}
                    for line in myfile:
                        l = line[0:len(line)-1]
                        elements = l.split('=')
                        property = {str(elements[0]):str(elements[1])}                
                        self.properties.update(property)
        else:
            print 'SM_PROP_DIR envvar not defined, aborting'
            sys.exit()
    
    def get(self,prop):
        return self.properties.get(prop)
