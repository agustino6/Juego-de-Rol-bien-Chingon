# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:56:23 2014

@author: Fernando
"""
#puntos de nivel
puntos_lvl = 8
vida=0
ataque=0
defensa=0
evasion=0
print "inicia tu epica aventura, tienes 4 habilidades que puedes subir de nivel con un maxicmo de 10 puntos cada una."
print "al inicio del juego puedes se te otorgan 8 puntos que podras repartir entre las siguientes habilidades:"
print "1) Vida"
print "2) defensa"
print "3) ataque"
print "4) evasion"
print "Que niveles quieres subir(tienes que gastar todos los puntos)"
while puntos_lvl > 0:
    print "Que niveles quieres subir(tienes que gastar todos los puntos)"
    opcion=raw_input
    if opcion ==1:
        print "cuantos puntos deseas agregar a vida?"
        puntos_add=raw_input
        vida =vida+ raw_input
    elif opcion ==2:
        print "cuantos puntos deseas agregar a defensa?"
        puntos_add=raw_input
        defensa =vida+ raw_input
    elif opcion== 3:
        print "cuantos puntos deseas agregar a ataque?"
        puntos_add=raw_input
        ataque =vida+ raw_input
    elif opcion ==4:
        print "cuantos puntos deseas agregar a evasion?"
        puntos_add=raw_input
        evasion =vida+ raw_input
    print "te quedan", puntos_lvl, "puntos para subir de nivel"
    