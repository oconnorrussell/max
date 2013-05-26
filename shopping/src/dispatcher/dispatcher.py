import emailEmitter

class dispatcher():
    
    def __init__(self):
        
        self.payload = None
        un = 'oconnor.russell'
        pw = '7gkW32iN'
        smtpServer = 'smtp.gmail.com:587'
        
        self.em = emailEmitter.emailEmitter(un, pw, smtpServer)
    
    def getEmailEmitter(self):
        return self.em
        
    def dispatchViaEmail(self, payload):
        from_addr = 'oconnor.russell@gmail.com'
        to_addr_list = 'oconnor.russell@gmail.com'
        cc_addr_list = ''
        subject = 'Wow it works'
        self.getEmailEmitter().emit(from_addr,to_addr_list, cc_addr_list,
            subject, payload)