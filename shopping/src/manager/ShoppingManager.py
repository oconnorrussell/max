from Tkinter import *
import Tkinter as ttk
import MySQLdb

from src.properties import propManager
from src.conns.mysql import mysqlConn
from src.logger import logger

class   ShoppingManager():

    def __init__(self):

        logger.info('x', 'b')

        logger.info('about to create the prop mgr')
        self.pm =   propManager.propertyManager()
        
        logger.info('about to create the mysql conn')
        self.conn   =  mysqlConn.mysqlConn()
                    
        self.recipes = []
        self.ingreds = {}      
        self.recipesIngredients = []
        
        root = Tk()
        root.title('Shopping Manager')
        
        logger.info('about to init ingredients')
        self.initIngreds()
        
        logger.info('about to ingest recipes ingredients')
        self.ingestRecipiesIngredients()                               

        logger.info('about to init recipes')
        self.initRecipes()
        
        #    add the processes frame to the root window
        self.frame   =   Frame(root,width=1000, height=200)
        self.frame.pack(expand=YES, fill=BOTH)
           
        #    add a canvas to the frame whose geometry manager is the grid.
        self.canv    =   Canvas(self.frame, relief=SUNKEN)

        #    size of the displayed view window
        self.canv.config( width=500,height=100)    
        
        self.recipesCanv = Canvas(self.canv, relief=SUNKEN, bg='Red')
        self.recipesCanv.config(width=300,height=200)
        
        self.recipesWidgetsCanv=Canvas(self.recipesCanv, bg='Yellow')
        self.recipesWidgetsCanv.config(width=200,height=400)
         
        #self.ingredsCanv = Canvas(self.canv, relief=SUNKEN, bg='Yellow')
        #self.ingredsCanv.config( width=500,height=100)
    
            
    def initRecipes(self):

        tmp =   []
        
        if  self.pm.get('USE_DB') == 'Y':
                    
            #    initialize a cursor on the connection.  a cursor is essentially a reference to a SELECT stmt and the rows that it returns once executed
            cur     =   self.mysqlConn.cursor()        

            #    load up the cursor with the SELECT stmt and execute it
            cur.execute('select recipe_id, recipe_name from recipes')

            for (row) in cur.fetchall():
                tmp.append({'id':row[0], 'name':row[1]})
        else:
            try:
                myfile = open(self.pm.get('RECIPES_FILE'), 'r')
            except:
                print "failed to find recipes, aborting"
                sys.exit
            else:                             
                for line in myfile:  
                    l = line[0:len(line)-1]
                    elements = l.split(',')
                    tmp.append({'id':elements[0], 'name':elements[1]})

        for r in tmp:
            temp_ingreds    =   []
            try:
                temp_ingreds = self.recipesIngredients[r['id']]
            except:
                temp_ingreds = {}       
            
            recipe = {'id':int(r['id']),
                      'name':r['id'], 
                      'ingreds':temp_ingreds,
                      'is_make':IntVar()
                     }
            self.recipes.append(recipe)
                                                                 
    def initIngreds(self):

        tmp =   []
        
        if  self.pm.get('USE_DB') == 'N':
            try:
                path    =   self.pm.get('INGREDIENTS_FILE')
                self.l.info('path=' + path)
                myfile = open(path, 'r')
            except:
                print "failed to find ingredients file, aborting"
                sys.exit()
            else:
                for line in myfile:  
                    l = line[0:len(line)-1]
                    elements = l.split(',')
                    tmp.append({'id':elements[0], 'name':elements[1], 'units':elements[2]})

        else:
     
            #    initialize a cursor on the connection.  a cursor is essentially a reference to a SELECT stmt and the rows that it returns once executed
            cur     =   self.oraConn.cursor()        

            #    load up the cursor with the SELECT stmt and execute it
            cur.execute('select ingred_id, ingred_name, ingred_uom from ingredients')
            #    iterate thru the rows of the cursor via the cur.fetchall method.  that method returns a list for each row.  each such list contains values corresponding to the columns in the SELECT clause

            for (row) in cur.fetchall():
                    tmp.append({'id':row[0], 'name':row[1], 'units':row[2]})
            
        for i in tmp:            
            ingred = {'name':i['name'],
                      'units':i['units'],
                      'is_needed':IntVar(),
                      'is_buy':IntVar(),
                      'total_req_qty':0,
                      'total_req_qty_disp':StringVar()}  

            self.ingreds[i['id']] = ingred
   
    def setReqQtys(self):
        
        for i in self.ingreds:
            self.ingreds[i]['total_req_qty']    =    0
        for r in self.recipes:
            if r['is_make'].get() == 1:
                for i in r['ingreds']:
                    self.ingreds[i]['total_req_qty']    +=    r['ingreds'][i]
        for i in self.ingreds:
            if self.ingreds[i]['total_req_qty'] >0:
                self.ingreds[i]['total_req_qty_disp'].set(str(self.ingreds[i]['total_req_qty']) + self.ingreds[i]['units'])
            
    
    def ingestRecipiesIngredients(self):

        tmp =   []
        
        if  self.pm.get('USE_DB') == 'N':
        
            try:
                myfile = open(self.pm.get('RECIPE_INGREDIENTS_FILE'), 'r')
            except:
                print "failed to find recipesingredients, aborting"
                sys.exit
            else:
                self.recipesIngredients = {}
                for line in myfile:  
                    l = line[0:len(line)-1]
                    elements = l.split(',')
                    recipeId = elements[0]
                    ingredId = elements[1]
                    qty = elements[2]
               
                    if recipeId in self.recipesIngredients:
                        print   'recipeId=' + str(recipeId) + ' exists'
                    else:
                        print   'adding recipeId=' + str(recipeId)
                        self.recipesIngredients[recipeId]    =   {}
                                        
                    self.recipesIngredients[recipeId][ingredId]  =   int(qty)
                
                print self.recipesIngredients 
        else:
            
            #    initialize a cursor on the connection.  a cursor is essentially a reference to a SELECT stmt and the rows that it returns once executed
            cur     =   self.conn.cursor()        

        #    load up the cursor with the SELECT stmt and execute it
            cur.execute('select recipe_id, ingred_id, qty from recipeingredients')
            #    iterate thru the rows of the cursor via the cur.fetchall method.  that method returns a list for each row.  each such list contains values corresponding to the columns in the SELECT clause

            for (row) in cur.fetchall():
                tmp.append({'rid':row[0],'iid':row[1],'q':row[2]})

        for ri in tmp:
            
            self.recipesIngredients = {}
            
            if ri['ri'] in self.recipesIngredients:
                print   'recipeId=' + str(recipeId) + ' exists'
            else:
                print   'adding recipeId=' + str(recipeId)
                self.recipesIngredients[ri['rid']]    =   {}
                                        
                self.recipesIngredients[ri['rid']][ri['iid']]  =   int(qty)
                         
    def dumpRecipes(self):
        i = 0
        #print self.recipes
        #print self.ingreds
        for r in self.recipes:
            print 'Recipe name = ' + r['name']
            #print r
            for i in r['ingreds']:
                print r['name'] + ' ingred = ' + self.ingreds[i]['name'] + ' Qty =' + str(r['ingreds'][i])
                                               
    def dumprecipesIngredients(self):
        print self.recipesIngredients.__str__()
    
    def handleRecipeSelecions(self):
        self.setReqQtys()
        self.renderIngredsCanvas()
   
    def renderIngredsCanvas(self):
        return
        i = self.ingredsCanv.gettags(self.ingredsCanv)
        print i              
        self.ingredsCanv.delete(self.ingredsCanv.find_all())
             
        myrow = 0
        mycol = 1    
        for i in self.ingreds:
              
            label = Label(self.ingredsCanv, text=self.ingreds[i]['name'])
            label.grid(row=myrow, column=mycol, sticky=W)
            
            chk =   Checkbutton(self.ingredsCanv, text="", variable=self.ingreds[i]['is_needed'])
            chk.grid(row=myrow, column=mycol+1, sticky=W)
            
            chk =   Checkbutton(self.ingredsCanv, text="", variable=self.ingreds[i]['is_buy'])
            chk.grid(row=myrow, column=mycol+2, sticky=W)
            
            label = Label(self.ingredsCanv,textvariable=self.ingreds[i]['total_req_qty_disp'])
            label.grid(row=myrow, column=mycol+3, sticky=W)
               
            myrow += 1
        for i in self.ingredsCanv.find_all():
                print 'john' + i                              

    def execute(self):

        proc = sys._getframe().f_code.co_name
        print   proc + ':' + 'Started'
                     
        myrow = 0
        mycol = 1
               
        for r in self.recipes:
            label   =   Label(self.recipesWidgetsCanv, text=r['name'])
            label.grid(row=myrow, column=mycol, sticky=W)
            chk =   Checkbutton(self.recipesWidgetsCanv, text="", variable=r['is_make'], command=self.handleRecipeSelecions)
            chk.grid(row=myrow, column=mycol+1, sticky=W)
                                     
            myrow += 1
        
              
        #    vertical scrollbar        
        #vert_sbar    =   Scrollbar(self.recipesCanv, orient='vertical')        
        #vert_sbar.config(command=self.recipesWidgetsCanv.yview)
        #self.recipesWidgetsCanv.config(yscrollcommand=vert_sbar.set)
        #vert_sbar.pack(side=RIGHT, fill=Y)
                    
        self.recipesCanv.pack()
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)
        
        
                   
if __name__ == '__main__':

        proc = sys._getframe().f_code.co_name
        print   proc + ':' + 'Started'

        print   'About to make the ShoppingManager'
        
        s   =   ShoppingManager()
             
        s.execute()
      
        #    put this here so we can call the execute upon refresh
        #print   'About to enter the main loop'
        s.frame.mainloop()
                    
        print   proc + ':' + 'Completed'