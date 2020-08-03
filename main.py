import gramatica as g
from gramatica import*
#"-4*-(3-5)"
raiz= g.Analizador("-4*-(3-5)")
Graficar(raiz)


def S(raiz):
    
    for hijo in raiz.getHijos():
          numero = E(hijo)
    return numero      

def E(raiz):
         
     if len(raiz.getHijos())== 3:
           hijo = raiz.getHijos()  
           if    hijo[1].Etiqueta == 'mas':
                      exp1=E(hijo[0])
                      exp2=E(hijo[2])
                      return exp1+exp2      
           elif  hijo[1].Etiqueta == 'menos':
                      exp1=E(hijo[0])
                      exp2=E(hijo[2])
                      return exp1-exp2
           elif  hijo[1].Etiqueta == 'por':
                      exp1=E(hijo[0])
                      exp2=E(hijo[2])
                      return exp1*exp2  
           elif  hijo[1].Etiqueta == 'div':   
                      exp1=E(hijo[0])
                      exp2=E(hijo[2])
                      if exp2==0:
                         return 'Error Semantico error division entre cero no exite'
                      return exp1/exp2

     elif len(raiz.getHijos())== 2:
               hijo = raiz.getHijos()
               if  hijo[0].Etiqueta == 'menos':
                      exp1=E(hijo[1])
                      return -int(exp1)
                       
     elif len(raiz.getHijos())== 1:
         hijo = raiz.getHijos()
         if hijo[0].Etiqueta == 'E':
             return E(hijo[0]) 
         else:    
             return hijo[0].Valor 


print("El resultado es de",S(raiz)) 