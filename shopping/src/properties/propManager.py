import sys

class propertyManager():
    
    def __init__(self):
        try:
            myfile = open('C:\\Users\\Dee\\Dropbox\\python-projects\\rjr-e\\shopping\\props-file\\propertyfile.dat', 'r')
        except:
            print "failed to find recipes, aborting"
            sys.exit
        else:
            self.properties = {}
            property = {}
            for line in myfile:
                l = line[0:len(line)-1]
                elements = l.split('=')
                property = {str(elements[0]):str(elements[1])}                
                self.properties.update(property)
            print self.properties
    def get(self,prop):
        return self.properties.get(prop)
