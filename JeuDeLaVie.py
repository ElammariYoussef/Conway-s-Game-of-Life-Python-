# Projet Réalisé par ELAMMARI Youssef et KICHOU Lisa

import random
import tkinter
import time

class jeu:
    def __init__(self,l,c):
        self.l = l
        self.c = c
        self.liste = []
        self.mort = '-'
        self.vivant = '+'
        self.something = ['-','+']
        self.new_list =[]
        self.motifVivant = 0
        self.value = False
        
    def RandomModeA(self):    
        for i in range(self.l):
            sous_ligne = []
            for j in range(self.c):
                sous_ligne.append(self.something[random.randint(0,1)])
            self.liste.append(sous_ligne)
            
    def RandomMode(self,nombrev):
        x = 0
        y = 0    
        for i in range(self.l):
            sous_ligne = []
            for j in range(self.c):
                 sous_ligne.append(self.something[0])
            self.liste.append(sous_ligne)
        while self.Tester() < nombrev:
            x = random.randint(0,len(self.liste)-1)
            y = random.randint(0,len(self.liste)-1)
            self.liste[x][y] == '-'
            self.liste[x][y] = '+'
    
    def Tester(self):
        var = 0
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if self.liste[i][j] == '+':
                    var +=1
        return var
    
    def newGen(self):
        old_list = []
        for i in range(len(self.liste)) :
            sous_old = []
            for j in range(len(self.liste[i])):
                sous_old.append(self.liste[i][j])
            old_list.append(sous_old)
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if self.liste[i][j] == '-' and self.nbradj(i,j) == 3:
                    self.liste[i][j] = '+'
                elif self.liste[i][j] == '+' and (self.nbradj(i,j) < 2 or self.nbradj(i,j) > 3):
                    self.liste[i][j] = '-'
        return old_list == self.liste
    
    def nbradj(self,x,y):
            Compteur=0
            if self.LesCoordonneesValides(x-1,y-1) and self.liste[x-1][y-1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x-1,y) and self.liste[x-1][y]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x-1,y+1) and self.liste[x-1][y+1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x,y-1) and self.liste[x][y-1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x,y+1) and self.liste[x][y+1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x+1,y+1) and self.liste[x+1][y+1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x+1,y-1) and self.liste[x+1][y-1]=='+':
                Compteur += 1
            if self.LesCoordonneesValides(x+1,y) and self.liste[x+1][y]=='+':
                Compteur += 1

            return Compteur
        
            
    def Afficher(self):
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                print(self.liste[i][j], end = ' ')
            print()
    
    
    def LesCoordonneesValides(self,x,y):
        return 0 <= x <self.l and 0 <= y <self.c
    
        
    

class Interface :
    def __init__(self):
        
        self.mainF = tkinter.Tk()
        self.mainF.title("The Game of Life")
        
        self.vivantImg = tkinter.PhotoImage(file = '1.png')
        self.mortImg = tkinter.PhotoImage(file = '0.png')
        
        self.lblchoix = tkinter.Label(self.mainF,text = "Entrez le nbr de lignes et de colonnes")
        self.lblchoix.pack()
        
        self.entryColumn = tkinter.Entry(self.mainF)
        self.entryColumn.pack()
        
        self.entryLine = tkinter.Entry(self.mainF)
        self.entryLine.pack()
        
        self.rpr = 0
        
        def newGen():
            if self.game.newGen():
                
                self.lbl_end = tkinter.Label(self.mainF,text = "La structure ci-dessus est stable, Le jeu est terminé !")
                self.lbl_end.pack()
                self.rpr +=1
                if self.rpr >1:
                    self.lbl_end.destroy()
            else:
                self.cnv.destroy()
                self.game.newGen()
                self.cote = 75
                self.pad = 5
                self.side = self.cote+ self.pad *2
                self.LARG = self.column * self.side
                self.HAUT = self.line * self.side
                self.cnv = tkinter.Canvas(self.mainF,width=self.LARG, height=self.HAUT, background ='gray')
                self.cnv.pack()
                X0 = Y0 = self.side/2
                for lig in range(self.line):
                    for col in range(self.column):
                        centre = (col*self.side+X0,lig*self.side+Y0)
                        if self.game.liste[lig][col] == '+':
                            self.cnv.create_image(centre,image = self.vivantImg)
                        else :
                            self.cnv.create_image(centre,image = self.mortImg)
                
            
        def Affichage():
                        
            self.new_gen2 = tkinter.Button(self.mainF,text = "Cliquez pour une nouvelle génération",command = newGen)
            self.new_gen2.pack()
            
            self.nbvivant1 = int(self.nbvivant.get())
            self.game = jeu(self.line,self.column)
            self.game.RandomMode(self.nbvivant1)
            self.cote = 75
            self.pad = 5
            self.side = self.cote+ self.pad *2
            self.LARG = self.column * self.side
            self.HAUT = self.line * self.side
            self.cnv = tkinter.Canvas(self.mainF,width=self.LARG, height=self.HAUT, background ='gray')
            self.cnv.pack()
            X0 = Y0 = self.side/2
            for lig in range(self.line):
                for col in range(self.column):
                    centre = (col*self.side+X0,lig*self.side+Y0)
                    if self.game.liste[lig][col] == '+':
                        self.cnv.create_image(centre,image = self.vivantImg)
                    else :
                        self.cnv.create_image(centre,image = self.mortImg)
                        
            self.ButtonValider2.destroy()
            self.lblvivant.destroy()
            self.nbvivant.destroy()
            
            

        def randomM():
            
            self.new_gen = tkinter.Button(self.mainF,text = "Cliquez pour une nouvelle génération",command = newGen)
            self.new_gen.pack()
            
            self.choixPartie.destroy()
            self.buttonAle.destroy()
            self.buttonMo.destroy()
            
            self.game = jeu(self.line,self.column)
            self.game.RandomModeA()
            self.cote = 75
            self.pad = 5
            self.side = self.cote+ self.pad *2
            self.LARG = self.column * self.side
            self.HAUT = self.line * self.side
            self.cnv = tkinter.Canvas(self.mainF,width=self.LARG, height=self.HAUT, background ='gray')
            self.cnv.pack()
            X0 = Y0 = self.side/2
            for lig in range(self.line):
                for col in range(self.column):
                    centre = (col*self.side+X0,lig*self.side+Y0)
                    if self.game.liste[lig][col] == '+':
                        self.cnv.create_image(centre,image = self.vivantImg)
                    else :
                        self.cnv.create_image(centre,image = self.mortImg)
                       

            
   
        def motiMode():
    
            self.choixPartie.destroy()
            self.buttonAle.destroy()
            self.buttonMo.destroy()
            
            self.lblvivant = tkinter.Label(self.mainF,text = "Saisir le nombre de case vivantes" )
            self.lblvivant.pack()
        
            self.nbvivant = tkinter.Entry(self.mainF)
            self.nbvivant.pack()
            self.ButtonValider2 = tkinter.Button(self.mainF,text = "valider", command=Affichage)
            self.ButtonValider2.pack()
            

        def PartieCommence():
            self.column = int(self.entryColumn.get())
            self.line = int(self.entryLine.get())
    
            emListe = []
    
            self.lblchoix.destroy()
            self.entryColumn.destroy()
            self.entryLine.destroy()
            self.ButtonValider.destroy()
            
            self.choixPartie = tkinter.Label(self.mainF, text = "  prenez votre choix  ")
            self.choixPartie.pack()
    
            self.buttonAle = tkinter.Button(self.mainF, text = "Mode Aleatoire", command = randomM)
            self.buttonAle.pack()
    
            self.buttonMo = tkinter.Button(self.mainF, text = " Mode Motif Aleatoire", command = motiMode)
            self.buttonMo.pack()
            
            
        self.ButtonValider = tkinter.Button(self.mainF,text = "start", command = PartieCommence)
        self.ButtonValider.pack()
        
        
        
app = Interface()
