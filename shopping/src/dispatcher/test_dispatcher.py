import dispatcher
import filePayload


d = dispatcher.dispatcher()
p = filePayload.filePayload('c:\\temp\\log_file.txt')
d.dispatchViaEmail(p)