import smtplib
import sys
#from logger import logger

#def sendEmail(from_addr, to_addr_list, cc_addr_list,
#    subject, message,
#    login, password,
#    smtpserver='smtp.gmail.com:587'):
#    header  = 'From: %s\n' % from_addr
#    header += 'To: %s\n' % ','.join(to_addr_list)
#    header += 'Cc: %s\n' % ','.join(cc_addr_list)
#    header += 'Subject: %s\n\n' % subject
#    message = header + message
#    server = smtplib.SMTP(smtpserver)
#    server.starttls()
#    server.login(login,password)
#    problems = server.sendmail(from_addr, to_addr_list, message)
#    server.quit()
#
#
#
#sendEmail(from_addr    = 'oconnor.russell@gmail.com', 
#    to_addr_list = ['oconnor.russell@gmail.com'],
#    cc_addr_list = ['oconnor.russell@gmail.com'], 
#    subject      = 'SHOPPING FILE LOGFILE.TXT', 
#    message      = str(messagetext), 
#    login        = 'oconnor.russell', 
#    password     = '')
#
#
#class    payload():
#    def __init__(self, payload):
#        self.message = payload
#    def set(self):
#        return
#
#class   atachment(payload):
#    ## handles email content in the form of attached files
#    def __init__(file):
#        return
#
class   textEmailPayload():
    # handles email content set in body
    def __init__(self, txt):
        self.txt    =    txt
    def set(self, txt):
            # -    set the text
            self.txt = txt
    def get(self):
            #-    returns the text
            return self.txt
        
class   suppliedStringEmailPayload(textEmailPayload):
    def __init__(self):
        pass
    def readText(self, supp):
        textEmailPayload.__init__(self, supp)
             
class   textEmailPayloadFromFile(textEmailPayload):
    #    handles email content set in body read from supplied file
    def __init__(self):
        #    reads the file, prep the msg string and calls set of base class
        pass
    def readFile(self, path):
            try:
                myfile = open(path)
            except:
                print 'file does not exist'
                sys.exit()
            else:
                lines = []
                txt = ''
                for line in myfile:
                    lines.append(line)
                for l in lines:
                    txt = txt + l
                textEmailPayload.__init__(self, txt)

class   emailer():
    def __init__(self):
        pass
    def send(self, payload):
       print payload
       
        
if __name__ == '__main__':
    
    e = emailer()
    t = suppliedStringEmailPayload()
    t.readText('hello sending text string')
    e.send(textEmailPayload.get(t))
#    p = textEmailPayloadFromFile()
#    p.readFile('c:\\temp\\log_file.txt')
#    e.send(textEmailPayload.get(p))
    
    
#    
#    def __init__(self):
#        ##    -    calls the setters that fetch the prop values
#        self.from       =  None
#        self.to         =  None
#        self.cc         =  None
#        self.smtpserver =  None
#
#       
#        self.from    =     _setFrom()
#        _setTo()
#        self.to
#        _setCC()
#        self.cc
#        _setSMTPServer()
#        self.smtpserver
#        setPayload()
#        prepMessage()
#        send()    - preps message and sends
#        
#class    senderOfSomethings():
#    
#
#send(something)
#e =    emailer()
#if classOf(something) == 'str':
#
#p    =    textEmailPayload(something)
#
#elseif    classOf(something) == 'file':
#p.textEmailPayloadFromFile(something)
#e.send(p)
#
#Case 0:    construct a string and send it
#
#e    =    emailer()
#
#p    = textEmailPayload("hello world")
#
#e.setPayLoad(p)
#
#e.send()
#
#
#
#Case 1:    read file and send as body of the email
#
#e    =    emailer()
#
#p    =    textEmailPayloadFromFile(file)
#
#e.setPayLoad(p)
#
#e.send()
#
#
#
#
#Case 2:    send the file as an attachment
#
#
#e    =    emailer()
#
#p    =    attachment(file)
#
#e.setPayLoad(p)
#
#e.send()
#



