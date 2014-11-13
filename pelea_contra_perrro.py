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

print "¿Qué escoges?" 
print "Cuentas con 15 de vida y 10 de maná"
print  "1) Ataque básico"
print  "2) Habilidad especial escupitajo ,6 maná"
print  "3) Usar item [Llaves]"
print  "4) huir "

vidaperro=10
vidausuario=15
mana=10
while vidaperro>0 or vidausuario>0:
   print "cuentas con ",vidausuario, " puntos de vida"
   print "cuentas con ",mana, "puntos de mana
     usuario=input()
    
    
     if usuario==1:
        
        atkusuario=random.randrange(1,6)
        atkperro= random.randrange(1,4)
        vidausuario=vidausuario-atkperro
        vidaperro=vidaperro-atkusuario
        
        print "Perro responde con morida letal causando",atkperro, "de daño"
        print "Ataque básico causó" ,atkusuario, "de daño"
        
     if usuario==2:
        mana=mana-6
        atkusuario=random.randrange(5,8)
        atkperro= random.randrange(1,4)
        vidaperro=vidaperro-atkusuario
        vidausuario=vidausuario-atkperro
        print "Perro causa ",atkperro," puntos de daño"
        print "Ataque especial causó ",atkusuario," de daño"
        
     if usuario==3:
         atkperro= random.randrange(1,4)
         vidausuario=vidausuario-atkperro
         print "Perro usa mordida y causa ",atkperro, "puntos de daño"
         print "Usaste item llaves pero no sirve para nada"
     if usuario==4:
         break
        
        
print "Terminaste la batalla con", vidausuario ," puntos de vida"
        
    
    
    