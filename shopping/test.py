from src.myLogging import  myLogger

def foo():
    print   'foo started'
    myLogger.info('info call')

if __name__ == '__main__':
    print 'x'
    foo()
    
