from Clases.Enemigo import Enemigo
from Funciones.Ficheros import *
from Funciones.Juego import *
from Funciones.OtrasFuciones import *


# Menú de inicio, permite acceder al login y al registro
def menuInicio():
    while True:
        cabeceraMenu("MENÚ PRINCIPAL")

        print("1.Login\n"
              "2.Registro\n"
              "0.SALIR\n")

        opcion_main = input("Elige: ")
        if opcion_main == "1":
            menuLogin()
            break
        elif opcion_main == "2":
            menuRegistro()
            break
        elif opcion_main == "0":
            escritura("Saliendo del juego.", True)
            exit()
        else:
            print("Introduce una opción correcta.")


# Menú de registro, permite regsitrar un usuario con nombre y contraseña
def menuRegistro():
    cabeceraMenu("REGISTRO")

    # NICK
    nick = input("Elige un nick: ")
    existe_nick = comprobarNick(nick)

    while existe_nick:
        cabeceraMenu("REGISTRO")
        escritura("El nick ya existe.")
        print()
        nick = input("Elige otro nick: ")
        existe_nick = comprobarNick(nick)

    # PASSWORD
    password = input("Introduce una contraseña: ")
    password_r = input("Repite la contraseña: ")

    while password != password_r:
        cabeceraMenu("REGISTRO")
        escritura("Las contraseñas no conciden.")
        print()
        password = input("Introduce una contraseña: ")
        password_r = input("Repite la contraseña: ")

    # Guarda en CSV
    guardarUsuario(nick, password)
    # Crea objeto y lo guarda
    jugador = Jugador(nick)
    guardarPartida(jugador)
    # Redirecciona menú partida
    menuPartida(jugador)


# Menú de login, permite loguear un usuario con nombre y contraseña
def menuLogin():
    cabeceraMenu("LOGIN")

    # NICK
    nick = input("Introduce tu nick: ")
    existe_nick = comprobarNick(nick)

    while not existe_nick:
        escritura("El nick no ha sido registrado.", limpiar=True)
        cabeceraMenu("LOGIN")
        nick = input("Vuelve a escribir tu nick (0 para ir atrás): ")
        if nick == "0":
            menuInicio()
        existe_nick = comprobarNick(nick)

    # PASSWORD
    password = input("Introduce tu contraseña: ")
    existe_password = comprobarPass(nick, password)

    while not existe_password:
        escritura("Contraseña incorrecta.", limpiar=True)
        cabeceraMenu("LOGIN")
        password = input("Vuelve a escribir tu contraseña: ")
        existe_password = comprobarPass(nick, password)

    # Lee la partida
    jugador = leerPartida(nick)
    menuPartida(jugador)


# Menú de partida, permite al usuario: luchar, acceder a la tienda, comprobar estadísticas, guardar y resetear el
# guardado
def menuPartida(jugador):
    while True:
        cabeceraMenu("PARTIDA")
        jugador.cabeceraSimple()
        print("\n1.Luchar\n"
              "2.Tienda\n"
              "3.Estadísticas\n"
              "4.Guardar\n"
              "5.Resetear partida guardada\n"
              "0.Atrás\n")

        opcion = input("Elige: ")
        if opcion == "1":
            menuLucha(jugador)
            break
        elif opcion == "2":
            menuTienda(jugador)
            break
        elif opcion == "3":
            menuEstadisticas(jugador)
            break
        elif opcion == "4":
            guardarPartida(jugador)
            jugador = leerPartida(jugador.nombre)
            escritura("Guardado correctamente.", limpiar=True)
            menuPartida(jugador)
            break
        elif opcion == "5":
            jugador_reset = resetearPartida(jugador)
            escritura("Partida reseteada correctamente.", limpiar=True)
            menuPartida(jugador_reset)
            break
        elif opcion == "0":
            menuInicio()
            break
        else:
            escritura("Introduce una opción correcta.")


# Menú de estadísticas, permite comprobar las estadísticas del jugador activo
def menuEstadisticas(jugador):
    while True:
        cabeceraMenu("ESTADÍSTICAS")
        jugador.cabecera()

        print("\n0.Atrás\n")

        opcion = input("Elige: ")
        if opcion == "0":
            menuPartida(jugador)
            break
        else:
            escritura("Introduce una opción correcta.")


# Menú de lucha, permite luchar o tomar poción al usuario con un enemigo aleatorio
def menuLucha(jugador):
    # Crea un enemigo aleatorio en funcion del nivel del jugadors
    enemigo = Enemigo(nivel_jugador=jugador.nivel)

    while True:
        cabeceraMenu("LUCHA")
        datosJugada(jugador, enemigo)

        print("1.Atacar\n"
              "2.Usar poción [%d]\n"
              "0.Abandonar\n" % jugador.pociones)

        opcion = input("Elige: ")

        if opcion == "1":
            if not atacar(jugador, enemigo):
                menuPartida(jugador)
        elif opcion == "2":
            if jugador.usarPocion():
                escritura("Has usado una poción. Recuperas %d de vida." % jugador.infoPocion())
            else:
                escritura("No tienes más pociones.")
        elif opcion == "0":
            print("Abandonando...")
            time.sleep(2)
            menuPartida(jugador)
        else:
            escritura("Introduce una opción correcta.")


# Menú de tienda, permite comprar pociones o subir de nivel con la experiencia adquirida
def menuTienda(jugador):
    while True:
        cabeceraMenu("TIENDA")
        jugador.cabeceraSimple()

        print("\n1.Comprar poción (15 exp) [+%d de vida]\n"
              "2.Subir nivel (%d exp) [+Ataque +EfectoPoción]\n"
              "0.Atrás\n" % (jugador.infoPocion(), jugador.experienciaNecesaria()))

        opcion = input("Elige: ")

        if opcion == "1":
            if jugador.comprarPociones():
                escritura("Has comprado una poción.")
            else:
                escritura("No tienes experiencia suficiente para comprar una poción.")
        elif opcion == "2":
            escritura(jugador.subirNivel())
        elif opcion == "0":
            escritura("Saliendo de la tienda.")
            menuPartida(jugador)
        else:
            escritura("Introduce una opción correcta.")