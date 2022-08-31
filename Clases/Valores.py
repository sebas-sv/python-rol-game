from random import randint
import names


# Refleja los limites inferiores y superiores de cada posible valor según el nivel
class Valores:

    def __init__(self):
        self.nombre_enemigo = names.get_last_name()

        self.valores_generales = {
            "pocion": {
                "precio": 15
            }
        }

        self.jugador_por_niveles = {
            1: {
                "ataque": randint(2, 4),
                "experienciaNecesaria": 50,
                "vidaPocion": 15
            },
            2: {
                "ataque": randint(4, 7),
                "experienciaNecesaria": 100,
                "vidaPocion": 20
            },
            3: {
                "ataque": randint(7, 10),
                "experienciaNecesaria": 300,
                "vidaPocion": 25
            },
            4: {
                "experienciaNecesaria": 9999
            }
        }

        self.enemigo_por_niveles = {
            1: {
                "vida": randint(6, 9),
                "ataque": randint(5, 10),
                "experienciaDada": randint(15, 25)
            },
            2: {
                "vida": randint(9, 15),
                "ataque": randint(10, 15),
                "experienciaDada": randint(25, 45)
            },
            3: {
                "vida": randint(15, 25),
                "ataque": randint(15, 25),
                "experienciaDada": randint(45, 70)
            },
            4: {
                "vida": randint(25, 50),
                # "ataque": randint(x, xx),
                "experienciaDada": randint(70, 90)
            }
        }
