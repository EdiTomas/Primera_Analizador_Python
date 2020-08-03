class Node():
    def __init__(self,Etiqueta="",Valor="",idNod=0):
        self.Etiqueta=Etiqueta
        self.Valor=Valor
        self.idNod=idNod
        self.hijos=[]

    def AddHijos(self,son):
       self.hijos.append(son)    

    def getHijos(self):
       return self.hijos


                 


