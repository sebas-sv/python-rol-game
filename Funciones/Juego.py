from Funciones.OtrasFuciones import escritura


# Devuelve las cabecera simple del jugador y el enemigo, se usa para el combate
def datosJugada(jugador, enemigo):
    return jugador.cabeceraSimple(), enemigo.cabeceraSimple()

# Acción de ataque
def atacar(atacante, atacado):
    ataque1 = atacante.atacar()
    escritura("Haces %d de daño." % ataque1)
    atacado.vida -= ataque1

    if atacado.vida > 0:
        ataque2 = atacado.atacar()
        escritura("Recibes %d de daño." % ataque2)
        atacante.vida -= ataque2
        if atacante.vida > 0:
            return True
        else:
            atacante.nivel = 1
            atacante.vida = 50
            atacante.pociones = 3
            atacante.experiencia = 0
            atacante.derrotas += 1
            escritura("Has perdido.")
            return False

    else:
        atacado.vida = 0
        experencia_ganada = atacado.darExperiencia()
        atacante.experiencia += experencia_ganada
        atacante.victorias += 1
        escritura("Has ganado %d puntos de exp." % experencia_ganada)
        return False
