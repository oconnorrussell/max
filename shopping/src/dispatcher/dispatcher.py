import emailEmitter

class Dispatcher():
    
    def __init__(self):
        
        self.payload = None
        self.em = emailEmitter('oconnor.russell', 'olknlknb', 'smtp.gmail.com:587')
    
    def getEmailEmitter(self):
        return self.em
        
    def dispatchViaEmail(self, payload):
        from_addr = 'oconnor.russell@gmail.com'
        to_addr_list = 'oconnor.russell@gmail.com'
        cc_addr_list = ''
        subject = 'Wow it works'
        self.getEmailEmitter().emit(from_addr,to_addr_list, cc_addr_list,
            subject, payload)