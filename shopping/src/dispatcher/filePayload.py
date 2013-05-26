import payload
from logger import logger

class filePayload(payload):
    
    def __init__(self, path):
        self.path = path
        try:
            myfile = open(path)
        except:
            logger.err('invalid path: ' + path)
            
        else:
            lines = []
            txt = ''
            for line in myfile:
                lines.append(line)
            for l in lines:
                txt = txt + l
                
            super.__init__(self,txt)