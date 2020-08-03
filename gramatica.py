from ply import lex
import ply.yacc as yacc
from Nodo import *
from graphviz import render
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
)

t_ignore = ' \t'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )
cont = 0
lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_inicio( p ):
    '''Inicio : expr 
    '''
    global cont
    raiz  = Node("S","",cont)
    cont  = cont+1
    raiz.AddHijos(p[1])    
    p[0] = raiz 

def p_operaciones( p ):
   '''expr : expr PLUS expr
        | expr MINUS expr  
        | expr TIMES expr
        | expr DIV expr 
   '''
   global cont
   if p[2]=='+':
        nodo  = Node("E","",cont)
        cont  = cont+1
        nodo1 = Node("mas",p[2],cont)
        cont  = cont+1
        nodo.AddHijos(p[1])
        nodo.AddHijos(nodo1)
        nodo.AddHijos(p[3])
        p[0] = nodo        
   elif p[2] == '-':

        nodo  = Node("E","",cont)
        cont  = cont+1
        nodo1 = Node("menos",p[2],cont)
        cont  = cont+1
        nodo.AddHijos(p[1])
        nodo.AddHijos(nodo1)
        nodo.AddHijos(p[3])
        p[0] = nodo 
   elif p[2]=='*': 
        
        nodo  = Node("E","",cont)
        cont  = cont+1
        nodo1 = Node("por",p[2],cont)
        cont  = cont+1
        nodo.AddHijos(p[1])
        nodo.AddHijos(nodo1)
        nodo.AddHijos(p[3])
        p[0] = nodo
   elif p[2]=='/':            
        nodo  = Node("E","",cont)
        cont  = cont+1
        nodo1 = Node("div",p[2],cont)
        cont  = cont+1
        nodo.AddHijos(p[1])
        nodo.AddHijos(nodo1)
        nodo.AddHijos(p[3])
        p[0] = nodo

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    global cont
    nodo  = Node("E","",cont)
    cont  = cont+1
    nodo1 = Node("menos",p[1],cont)
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(p[2])
    p[0] = nodo



def p_expr2NUM( p ) :
    'expr : NUMBER'
    global cont
    nodo  = Node("E","",cont)
    cont  = cont+1
    nd = Node("numero",p[1],cont)
    cont  = cont+1
    nodo.AddHijos(nd)
    p[0] = nodo


def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    global cont
    nodo  = Node("E","",cont)
    cont  = cont+1
    nodo.AddHijos(p[2])
    p[0] = nodo




def p_error( p ):
    print("Syntax error in input!")



parser = yacc.yacc()
def recorrerarbol(raiz):
        cuerpo = ""
        for  hijos in raiz.getHijos(): 
             if hijos.Valor != None : 
                cuerpo += "\"" + str(raiz.idNod) + "\"" + " [label=\"" + raiz.Etiqueta + "\"]"
                cuerpo += "\"" + str(hijos.idNod) + "\"" + " [label=\"" + str(hijos.Valor) + "\"]"
                cuerpo += "\"" + str(raiz.idNod) + "\" -> " + "\"" + str(hijos.idNod) + "\""
                cuerpo += recorrerarbol(hijos)
        return cuerpo

def Graficar(raiz):
        file = open("arbol.dot", "w")
        file.write(
                    " digraph G {\n"
                    + "     rankdir=TB; "
                    + "" + " node[ shape=record,  style=filled ,fillcolor=seashell2, fontcolor=black, color=coral1];  \n"
                    + "edge[color=chartreuse1] \n"
            )
        file.write(recorrerarbol(raiz))
        file.write("} \n")

        file.close()
        render('dot','jpg','arbol.dot')
       
def Analizador(Entrada=""):
  res = parser.parse(Entrada) # the input
  
  return res





