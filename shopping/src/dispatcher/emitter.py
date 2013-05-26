class emitter():
    
    def __init__(self):
        self.payload = None
        
    def setPayload(self, payload):
        self.payload = payload
    
    def getPayload(self):
        return self.payload