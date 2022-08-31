from Clases.Valores import Valores


class Jugador:
    def __init__(self, nombre, nivel=1, vida=50, pociones=3, experiencia=0, victorias=0, derrotas=0):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.pociones = pociones
        self.experiencia = experiencia
        self.victorias = victorias
        self.derrotas = derrotas

    def atacar(self):
        val = Valores()
        return val.jugador_por_niveles[self.nivel]["ataque"]

    def comprarPociones(self):
        val = Valores()
        if self.experiencia >= val.valores_generales["pocion"]["precio"]:
            self.pociones += 1
            self.experiencia -= val.valores_generales["pocion"]["precio"]
            return True
        else:
            return False

    def usarPocion(self):
        val = Valores()
        if self.pociones > 0:
            self.vida += val.jugador_por_niveles[self.nivel]["vidaPocion"]
            self.pociones -= 1
            return True
        else:
            return False

    def infoPocion(self):
        val = Valores()
        return val.jugador_por_niveles[self.nivel]["vidaPocion"]

    def experienciaNecesaria(self):
        val = Valores()
        return val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]

    def subirNivel(self):
        val = Valores()
        if self.nivel == 1 and self.experiencia >= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]:
            self.experiencia -= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]
            self.nivel += 1
            return "Has subido a nivel %d." % self.nivel
        elif self.nivel == 2 and self.experiencia >= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]:
            self.experiencia -= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]
            self.nivel += 1
            return "Has subido a nivel %d." % self.nivel
        elif self.nivel == 3 and self.experiencia >= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]:
            self.experiencia -= val.jugador_por_niveles[self.nivel]["experienciaNecesaria"]
            self.nivel += 1
            return "Has subido a nivel %d." % self.nivel
        elif self.nivel == 4:
            return "Nivel máximo."
        else:
            return "No tienes experiencia suficiente para subir de nivel."

    def cabecera(self):
        print("NICK:", self.nombre, "\nNIVEL:", self.nivel, "\nVIDA:", self.vida, "\nPOCIONES:", self.pociones
              , "\nEXPERIENCIA:", self.experiencia, "\nVICTORIAS:", self.victorias, "\nDERROTAS:", self.derrotas)

    def cabeceraSimple(self):
        print(self.nombre, "( LV:", self.nivel, ")\n",
              self.vida, "de vida\n",
              self.pociones, "pociones\n",
              self.experiencia, "de experiencia")