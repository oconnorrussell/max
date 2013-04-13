from Tkinter import *

root = Tk()


root.title('Demo Canvases')

#    one frame with sub-frames for each of the three areas laid out in columns that expand with the whole frame.

frame   =   Frame(root, bg='Green', bd=10)
frame.pack(expand=YES, fill=BOTH)

frameA  =   Frame(frame, bg='black', bd=10)
frameA.pack(expand=YES, fill=BOTH, side=LEFT)

recipesCanv   =   Canvas(frameA, bg='gray')
recipesCanv.pack(expand=YES, fill=BOTH, side=TOP)

recipeLabelsCanv   =   Canvas(recipesCanv)
recipeLabelsCanv.pack(side=LEFT)

for r in range(20):
    label   =   Label(recipeLabelsCanv, text='recipe ' + str(r))
    label.grid(row=r, column=0)
    chk =   Checkbutton(recipeLabelsCanv)
    chk.grid(row=r, column=1)

recipeLabelsCanv.config(scrollregion=recipeLabelsCanv.bbox(ALL))

#    vertical scrollbar        
vert_sbar    =   Scrollbar(recipeLabelsCanv, orient='vertical', command=recipeLabelsCanv.yview)
recipeLabelsCanv.config(yscrollcommand=vert_sbar.set)
vert_sbar.pack(side=RIGHT, expand=YES, fill=Y)

#    horiz scrollbar
#horiz_sbar    =   Scrollbar(recipesCanv, orient='horizontal')
#horiz_sbar.config(command=recipesCanv.xview)
#recipesCanv.config(xscrollcommand=horiz_sbar.set)
#horiz_sbar.grid()
                                     

#recipeIngredsCanv   =   Canvas(frameA, bg='magenta')
#recipeIngredsCanv.pack(expand=YES, fill=BOTH, side=TOP)

frameB  =   Frame(frame, bg='Yellow', bd=10)
frameB.pack(expand=YES, fill=BOTH,side=LEFT)

ingredsCanv   =   Canvas(frameB, bg='purple')
ingredsCanv.pack(expand=YES, fill=BOTH)


frameC  =   Frame(frame, bg='Blue', bd=10)
frameC.pack(expand=YES, fill=BOTH, side=LEFT)

shoppingListCanv   =   Canvas(frameC, bg='brown')
shoppingListCanv.pack(expand=YES, fill=BOTH)


frame.mainloop()

