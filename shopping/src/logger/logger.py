import sys

def _callersName():
    #    return the name of the caller
    return  sys._getframe(2).f_code.co_filename + ':' + str(sys._getframe(2).f_lineno) +  ':' + sys._getframe(2).f_code.co_name

def info(msg):
    _info(msg,_callersName())

def _info(msg, caller=None):
    #    caller is normally not supplied.  when called from within this module, the callers need to say what the actual caller is
    if caller == None:
        caller  =   _callersName()
    
    print 'info:' + caller + ':' + msg

def started():
    #    issue a started log message
    _info('Started', _callersName())

def completed():
    #    issue a completed log message
    _info('Completed', _callersName())

def err(msg):
    _err(msg,_callersName())

def _err(msg, caller=None):
    #    caller is normally not supplied.  when called from within this module, the callers need to say what the actual caller is
    if caller == None:
        caller  =   _callersName()
    print 'err:' + caller + ':' + msg