# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 17:46:11 2014

@author: Fran
"""

#pelea contra el perro




import random

print "Elegiste pelear contra el perro"

print""
print""
print "Perro nivel 1, vida 10"

money=50
vidaperro=10
vidausuario=15
mana=10


while vidaperro>0 and vidausuario>0:
  
 print "Perro cuenta con", vidaperro, " puntos de vida"   
 print "cuentas con ",vidausuario, " puntos de vida" 
 print "cuentas con ",mana, "puntos de mana"
 print  "1) Ataque básico"
 print  "2) Habilidad especial escupitajo ,6 maná"
 print  "3) Usar item [Llaves]"
 print  "4) huir "
 
 usuario=input()
    
    
 if usuario==1:
        
    atkusuario=random.randrange(1,6)
    atkperro= random.randrange(1,3)
    vidausuario=vidausuario-atkperro
    vidaperro=vidaperro-atkusuario
        
    print "Perro responde con morida letal causando",atkperro, "de daño"
    print "Ataque básico causó" ,atkusuario, "de daño"
    
        
 elif usuario==2:
    if mana<6:
        print "No cuentas con mana suficiente"
    else:    
     mana=mana-6
     atkusuario=random.randrange(5,8)
     atkperro= random.randrange(1,3)
     vidaperro=vidaperro-atkusuario
     vidausuario=vidausuario-atkperro
     print "Perro causa ",atkperro," puntos de daño"
     print "Ataque especial causó ",atkusuario," de daño"
     
        
 elif usuario==3:
     atkperro= random.randrange(1,3)
     vidausuario=vidausuario-atkperro
     print "Perro usa mordida y causa ",atkperro, "puntos de daño"
     print "Usaste item llaves pero no sirve para nada"
     
 elif usuario==4:
     print "Huir tiene sus consecuencias"
     money=money-5
     print "Ahora tienes ", money , " pesos"
     break
     
         
        
print "Enemigo perro ha sido derrotado"        
print "Terminaste la batalla con", vidausuario ," puntos de vida"
        
    
    
    