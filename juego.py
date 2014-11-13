# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 18:59:48 2014

@author: Rafael
"""

from creacionpersonaje import *

def main():
    print "inicia tu epica aventura, tienes 4 habilidades que puedes subir de nivel con un maxicmo de 10 puntos cada una.\n"
    print "al inicio del juego puedes se te otorgan 8 puntos que podras repartir entre las siguientes habilidades(cada habilidad tiene un valor inicial de 5):"
    print "a) Vida: Si la pierdes toda, te mueres."
    print "b) Defensa: Reduce el daño que tomas por ataque."
    print "c) ataque: Aumenta el daño que haces."
    print "d) Evasion: Aumenta tu probablidad de esquivar un ataque."
    raw_input('Presiona enter para continuar')
    os.system('cls')
    
    jugador = crear_personaje([5,5,5,5,50],8)
    inventario = []
    os.system('cls')
    escribir_stats(jugador)
    
    #por hacer: TODO
main()