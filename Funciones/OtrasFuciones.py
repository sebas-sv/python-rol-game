import os
import sys
import time

CLEAR = 'cls' if sys.platform == 'win32' else 'clear'


def escritura(mensaje, limpiar=False, tiempo=0.05):
    if limpiar:
        print(CLEAR)
        os.system(CLEAR)

    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != ".":
            time.sleep(tiempo)
        else:
            time.sleep(1)

    sys.stdout.write('\n')

    if limpiar:
        time.sleep(1)
        os.system(CLEAR)


def cabeceraMenu(nombre):
    os.system(CLEAR)
    print('{:*^50}'.format('*'))
    print('{:*^50}'.format('  ' + nombre + '  '))
    print('{:*^50}'.format('*'))
    print()
