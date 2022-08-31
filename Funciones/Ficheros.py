import csv
import json
import os

from datetime import datetime
from Clases.Jugador import Jugador

# Constantes de los nombres de los ficheros
FICHERO_USUARIOS = "Ficheros/usuarios.csv"
FICHERO_PARTIDAS = "Ficheros/partidas.json"


# Crea los ficheros si no existe
def crearFicheros():
    if not os.path.exists(FICHERO_USUARIOS):
        # Crea fichero CSV con la cabecera: NOMBRE, CLAVE, CREATED etc...
        with open(FICHERO_USUARIOS, "w") as fichero:
            contenido = csv.writer(fichero)
            contenido.writerow(['NOMBRE', 'PASSWORD', 'CREATED'])
    if not os.path.exists(FICHERO_PARTIDAS):
        # Crea fichero JSON con clave 'partidas' y contenido (array vacío)
        with open(FICHERO_PARTIDAS, "w") as fichero:
            contenido = {"partidas": []}
            json.dump(contenido, fichero, indent=4)  # Dump con identación


# Comprueba si existe el nombre de usuario en el fichero CSV
def comprobarNick(nick):
    with open(FICHERO_USUARIOS, "r") as fichero:
        existe = False
        try:
            contenido = csv.reader(fichero)
            for fila in contenido:
                if fila[0] == nick:
                    existe = True
                    break
        except:
            pass
        finally:
            return existe


# Comprueba la constraseña del usuario de usuario en el fichero CSV
def comprobarPass(nick, password):
    with open(FICHERO_USUARIOS, "r") as fichero:
        contenido = csv.reader(fichero)
        existe = False
        for fila in contenido:
            if fila[0] == nick and fila[1] == password:
                existe = True
                break
        return existe


# Guarda el usuario, su clave y la fecha de creación en un fichero CSV
def guardarUsuario(nick, password):
    # 'a' evita sobreescribir el fichero como haría w
    with open(FICHERO_USUARIOS, "a") as fichero:
        contenido = csv.writer(fichero)
        contenido.writerow([nick, password, datetime.now()])


# Lee los datos de la partida depasándole el nombre de usuario
def leerPartida(nick):
    with open(FICHERO_PARTIDAS) as fichero:
        contenido = json.load(fichero)
        partidas = contenido['partidas']
        partida = None

        # Recorre la lista de partidas
        for fila in partidas:
            # Si encuentra al jugador crea su objeto
            if nick in fila['nombre']:
                partida = fila

    return Jugador(partida['nombre'], partida['nivel'], partida['vida'], partida['pociones'], partida['experiencia'],
                   partida['victorias'], partida['derrotas'])


# Función auxiliar de la función 'guardarPartida' para guardar archivos JSON
def guardarJson(contenido):
    with open(FICHERO_PARTIDAS, 'w') as fichero:
        json.dump(contenido, fichero, indent=4)
        return True


# Guarda los datos de la partida actual en el fichero JSON, sobreescribe si ya existe el usuario
def guardarPartida(jugador):
    with open(FICHERO_PARTIDAS) as fichero:
        contenido = json.load(fichero)
        partidas = contenido['partidas']

        existe = False

        # Recorre la lista de partidas
        for fila in partidas:
            # Si encuentra al jugador actualiza sus datos
            if jugador.nombre in fila['nombre']:
                existe = True
                fila['nivel'] = jugador.nivel
                fila['vida'] = jugador.vida
                fila['pociones'] = jugador.pociones
                fila['experiencia'] = jugador.experiencia
                fila['victorias'] = jugador.victorias
                fila['derrotas'] = jugador.derrotas
                guardarJson(contenido)
                break

        # Si no lo encuentra, crea una partida
        if not existe:
            partidas.append(jugador.__dict__)
            guardarJson(contenido)


# Resetea los datos de la partida pasándole un nombre de usuario
def resetearPartida(jugador):
    with open(FICHERO_PARTIDAS) as fichero:
        contenido = json.load(fichero)
        partidas = contenido['partidas']

        # Recorre la lista de partidas
        for fila in partidas:
            # Si encuentra al jugador actualiza sus datos
            if jugador.nombre in fila['nombre']:
                fila['nivel'] = 1
                fila['vida'] = 50
                fila['pociones'] = 3
                fila['experiencia'] = 0
                fila['victorias'] = 0
                fila['derrotas'] = 0
                guardarJson(contenido)
                break

    return Jugador(nombre=jugador.nombre)
