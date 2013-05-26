import emitter
import payload
import smtplib

class emailEmitter(emitter.emitter):
    
    def __init__(self, un, pwd, smtpServer):
        self.un = un
        self.pwd = pwd
        self.smtpServer = smtpServer
    
    def getSmtpServer(self):
        return self.smtpServer
    
    def getUserName(self):
        return self.un
    
    def getPassword(self):
        return self.pwd  
    
    def emit(self, from_addr,to_addr_list, cc_addr_list,
            subject, payload):
        
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + payload.getMessageStr()
        server = smtplib.SMTP(self.getSmtpServer())
        server.starttls()
        server.login(self.getUserName(),self.getPassword())
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        
    