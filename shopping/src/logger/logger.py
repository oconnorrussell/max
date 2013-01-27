import sys

def _callersName():
    #    return the name of the caller
    return  sys._getframe(2).f_code.co_filename + ':' + str(sys._getframe(2).f_lineno) +  ':' + sys._getframe(2).f_code.co_name

def info(msg, caller=None):
    #    caller is normally not supplied.  when called from within this module, the callers need to say what the actual caller is
    if caller == None:
        caller  =   _callersName()
        
    print   caller + ':' + msg

def started():
    #    issue a started log message
    info('Started', _callersName())

def completed():
    #    issue a completed log message
    info('Completed', _callersName())
