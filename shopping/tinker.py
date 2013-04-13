from Tkinter import *

root = Tk()
states=[]

def printStatus():
    print 'Started'
    print([var.get() for var in states])
    return 'foo'
print 'about to create button'
b=Button(root, text = 'Status', command = printStatus)
b.pack()
print 'command = ' + b.cget("command")
print 'button created'


for i in range(10):
    var=IntVar()
    var.set(1)
    chk = Checkbutton(root, text = str(i),variable = var).pack()
    states.append(var)

root.mainloop()

#import sys
#class firstClass:
#    def __init__(self):
#        self.data=None
#    def setdata(self,value):
#        self.data = value
#    def get(self):
#        return self.data
#
#x= firstClass()
#print x
#print sys.exit
#
#sys.exit()
#x.setdata(10)
#print x.get()

