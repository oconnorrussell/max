import smtplib

def sendEmail(from_addr, to_addr_list, cc_addr_list,
    subject, message,
    login, password,
    smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

try:
    print 'attempting to open log_file.txt'
    emailmessage = []
    myfile = open('c:\\temp\\log_file.txt')
    for line in myfile:
            emailmessage.append(line)
    print emailmessage
            
    messagetext = emailmessage
except:
    print 'file does not exist, exiting'
    sys.exit()

sendEmail(from_addr    = 'oconnor.russell@gmail.com', 
    to_addr_list = ['oconnor.russell@gmail.com'],
    cc_addr_list = ['oconnor.russell@gmail.com'], 
    subject      = 'SHOPPING FILE LOGFILE.TXT', 
    message      = str(messagetext), 
    login        = 'oconnor.russell', 
    password     = '')