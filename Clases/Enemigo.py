from random import randint

from Clases.Valores import Valores


class Enemigo:
    def __init__(self, nivel_jugador=1):
        self.nombre = self.asignarNombre()
        self.nivel_jugador = nivel_jugador
        self.nivel = self.asignarNivel()
        self.vida = self.asignarVida()

    def asignarNombre(self):
        val = Valores()
        return val.nombre_enemigo

    def asignarNivel(self):
        return randint(self.nivel_jugador, self.nivel_jugador + 1)

    def asignarVida(self):
        val = Valores()
        return val.enemigo_por_niveles[self.nivel]["vida"]


    def atacar(self):
        val = Valores()
        return val.enemigo_por_niveles[self.nivel]["ataque"]

    def darExperiencia(self):
        val = Valores()
        return val.enemigo_por_niveles[self.nivel]["experienciaDada"]

    def cabecera(self):
        print("\nENEMIGO:", self.nombre, "\nNIVEL:", self.nivel, "\nVIDA:", self.vida)

    def cabeceraSimple(self):
        print("\nENEMIGO:\n",
              self.nombre, "( LV:", self.nivel, ")\n",
              self.vida, "de vida\n\n\n")
