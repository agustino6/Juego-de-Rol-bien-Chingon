import os

def dialogo_puntos(jugador, opc,maximo):
    stats = ['vida','ataque','defensa','evasion']
    puntos = int(raw_input(("cuantos puntos deseas agregar a "+stats[opc]+"?[0,"+str(maximo)+"]")))
    while puntos>maximo:
        puntos = int(raw_input("valor fuera de rango. Introduce un valor en el rango [0,"+str(maximo)+"]"))
    jugador[opc] += puntos
    return maximo - puntos

def escribir_stats(jugador):
    stats = ['Vida','Ataque','Defensa','Evasion','Dinero']
    print 'Habilidades del jugador:'
    for i in range(4):
        print str(stats[i])+": "+str(jugador[i])

#en orden: vida, defensa, ataque, evasion, dinero.
def crear_personaje(jugador,puntos_lvl):
    while True:
        print"Selecciona la habilidad que quieres aumentar(debes agotar todos tus puntos):"
        print "1) Vida (" + str(jugador[0])+")"
        print "2) Defensa ("+ str(jugador[1])+")"
        print "3) Ataque (" + str(jugador[2])+")"
        print "4) Evasion (" + str(jugador[3])+")"
        opcion=int(raw_input('Elige una opcion: '))
    
        puntos_lvl = dialogo_puntos(jugador,opcion-1,puntos_lvl)
        
        if puntos_lvl>0:
            print "\nTe quedan", puntos_lvl, "puntos para subir de nivel, tienes que usar todos los puntos."
        else:
            print "\nHas terminado de crear a tu personaje."
            os.system('cls')
            break
    return jugador




